# Upwork - Entry Exam

## Goal

Working FastAPI API with a User and Profile models and schemas.

## Instructions

1. Fork this repository
2. Complete the tasks below adhering to the requirements
3. Submit a pull request with your solution in your forked repository
4. Deliver a GitHub repository with your solution (it can be private, just give access to @arielaco)

## Tasks

- [✅] Create a [User](###User) and [Profile](###Profile) models and schemas
- [ ] Develop a REST API exposing CRUD endpoints for both models
- [ ] Test at least 2 endpoints using pytest (with fixtures)
- [ ] Point docs to root path
- [ ] Create requirements file
- [ ] Add a section on `README.md` with setup (venv), install (pip), run and testing instructions

### User

- Email as username
- Can have multiple profiles
- Can have a list of favorite profiles

### Profile

- It has a name and a description
- Belongs to a user

## Requirements

- Use English for all code, comments, commit messages, and documentation
- Delete dead code (unrelated to tasks)
- All responses must be JSON
- Implement proper folder structure
- Validation must be done using Pydantic
- Use multiple commits (when possible, use conventional commit messages)
