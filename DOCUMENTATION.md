# Bizzbot 🤖 API Documentation

Detailed Documentation of the API's endpoints, as well as others concepts.

---

# Table of Contents
- [API Overview](#api-overview)
    - [Authentication](#authentication)
    - [Users](#users)

## API Overview 🔬

There are dozens of API endpoints, and each of them allow for a trailing backslash or not, depending on the preferences of the developer consuming the endpoints.

<br>

### Authentication

METHOD   | ENDPOINT                   | FUNCTIONALITY | DESCRIPTION
------   | -------------------------- | ------------- | -----------
_POST_   | `/api/auth/login/`         | Get a user's access and refresh tokens | Takes a set of user credentials (email and password) and returns an access and refresh JSON web token pair to prove the authentication of those credentials.
_POST_   | `/api/auth/login/refresh/` | Generate an access token from a refresh token | Takes a user's refresh token and generates a new access token from it and returns the access token.
_POST_   | `/api/auth/logout/`        | Blacklist a user's refresh token | Takes a user's refresh token and blacklists it, thereby invalidating it as a form of logout.

<br>

### Users

METHOD   | ENDPOINT           | FUNCTIONALITY | DESCRIPTION
------   | ------------------ | ------------- | -----------
_GET_    | `/api/users/`      | Get all users | This endpoint returns a paginated response of all users stored in the database, with all necessary fields.
_POST_   | `/api/users/`      | Create a user  | This endpoint accepts common parameters of a user, saves the user to the database and returns the created user.
_PUT_    | `/api/users/{pk}/` | Completely update a user | This endpoint accepts the id of a user as a path parameter, searches for the user in the database and returns the user.
_PATCH_  | `/api/users/{pk}/` | Partially update a user | This endpoint accepts the id of a user as a path parameter, searches for the user in the database, and attempts to update ALL fields of the user.
        
_DELETE_ | `/api/users/{pk}/` | Delete a user | This endpoint accepts the id of a user as a path parameter, searches for the user in the database and deletes the user completely.
