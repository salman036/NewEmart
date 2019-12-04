class Constant(object):
    GET = "GET"
    POST = "POST"
    REGISTER_SUCCESSFULLY = "Register Successfully"
    LOGIN_SUCCESSFULLY = "Login Successfully"
    INFO_FLASH_MESSAGE = "info"
    INVALID_EMAIL_OR_PASSWORD = "Invalid email or password"
    RESET_PASSWORD_EMAIL_SEND = "An email has been sent with instructions to reset your password."
    EXPIRE_TOKEN = "That is an invalid or expired token"
    PASSWORD_UPDATE = "Your password has been updated! You are now able to log in"
    USER_NAME_ALREADY_EXIST = "User Name is already exist"
    EMAIL_ALREADY_EXIST = "Email is already exist"
    EMAIL_DOES_NOT_EXIST = "Email does not exist"
    EMAIL = 'Email'
    USER_NAME = 'User Name'
    NAME = 'Name'
    PASSWORD = 'Password'
    CONFIRM_PASSWORD = "Confirm Password"
    RESET_PASSWORD = "Reset Password"
    SUBMIT = "Submit"
    INVALID_TOKEN = "Invalid or expire token"
    DANGER = 'danger'
    FLASH_MESSAGE_SUCCESS = 'success'
    SAVE_CATEGORY = 'Category Saved'
    NAME_ALREADY_EXIST = "Name already exist"
    DELETE_SUCCESSFULLY = "Delete Successfully."
    UPDATE_SUCCESSFULLY = "Update Successfully"
    UPLOAD_IMAGE = "Upload image"
    IMAGE_FILED_EMPTY = "Image preview is empty"
    SAVE_SUCCESSFULLY = "Save Successfully"
    REGULAR_EXPRESSION = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})"
    REGULAR_EXPRESSION_EMAIL = "^[a-z]{1,50}_?[0-9]{0,30}@gmail\.com$"
    REGULAR_EXPRESSION_MESSAGE = "Minimum eight characters, at least one uppercase letter," \
                                 "one lowercase letter, one number and one special character:"
    REGULAR_EXPRESSION_EMAIL_MESSAGE = "Email must be end with @gmail.com"


class Product():
    NAME = "Name"
    TOTAL_QUANTITY = "Total Quantity"
    UNIT = "Unit"
    IMAGE = "Image Upload"
    DESCRIPTION = "Description"
    NET_PRICE = "Net Price"
    SALE_PRICE = "Sale Price"
    TOTAL = "Total"
