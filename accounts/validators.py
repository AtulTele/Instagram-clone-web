
from django.contrib.auth.password_validation import (
    MinimumLengthValidator,
    CommonPasswordValidator,
    NumericPasswordValidator,
    UserAttributeSimilarityValidator,
)
from phonenumber_field.phonenumber import PhoneNumber
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth import get_user_model
from django.http import HttpResponse


def check_username_exists(request):
    """Validate whether the typed username exists."""

    username = request.POST.get("username", "")
    username_exists = (
        get_user_model()
        .objects.filter(username=username)
        .exists()
    )

    if username and username_exists:
        return HttpResponse(
            '<div class="error">This username exists!</div>'
        )
    elif not username or username.isspace():
        return HttpResponse(
            '<div class="error">Invalid username!</div>'
        )

    return HttpResponse(
        f'<div class="success">"{username}" is available.</div>'
    )


def email_address_validation(request):
    """Validate the email address and check for duplicates."""

    email = request.POST.get("email", "").strip()

    if get_user_model().objects.filter(email=email).exists():
        return HttpResponse(
            '<div class="error">Email address provided exists!</div>'
        )

    try:
        validate_email(email)
    except ValidationError:
        return HttpResponse(
            '<div class="error">Invalid email address!</div>'
        )

    return HttpResponse("")


def validate_phone_number(phone_number):
    """Parse and validate a phone number using India as the default region."""

    phone_number = (phone_number or "").strip()

    if not phone_number:
        raise ValidationError("Please enter your mobile number.")

    try:
        parsed_number = PhoneNumber.from_string(
            phone_number,
            region="IN",
        )

        if not parsed_number.is_valid():
            raise ValidationError("Invalid mobile number!")

    except ValidationError:
        raise
    except Exception as exc:
        raise ValidationError("Invalid mobile number!") from exc

    return None


def mobile_number_validation(request):
    """Validate the mobile number provided by the user."""

    mobile_number = request.POST.get("phone_no", "")

    try:
        validate_phone_number(mobile_number)
    except ValidationError as error:
        message = " ".join(error.messages)
        return HttpResponse(
            f'<div class="error">{message}</div>'
        )

    return HttpResponse(
        '<div class="success">Phone number is valid.</div>'
    )


def validate_password_with_django_validators(password):
    """Validate passwords using Django's built-in validators."""

    validators = [
        MinimumLengthValidator(),
        CommonPasswordValidator(),
        NumericPasswordValidator(),
        UserAttributeSimilarityValidator(),
    ]

    errors = []

    for validator in validators:
        try:
            validator.validate(password)
        except ValidationError as error:
            errors.extend(error.messages)

    return errors


def password_match_and_length_validation(request):
    """Validate password strength and matching confirmation."""

    password1 = request.POST.get("password1", "")
    password2 = request.POST.get("password2", "")

    if not password1:
        return HttpResponse(
            '<div class="error">Please enter a password.</div>'
        )

    errors = validate_password_with_django_validators(password1)

    if errors:
        error_message = "<br>".join(errors)
        return HttpResponse(
            f'<div class="error">{error_message}</div>'
        )

    if password2 and password1 != password2:
        return HttpResponse(
            '<div class="error">Passwords didn\'t match</div>'
        )

    return HttpResponse(
        '<div class="success">You\'re good to go!</div>'
    )
