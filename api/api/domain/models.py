from dataclasses import dataclass


@dataclass
class Question:
    # question_id: str
    text: str
    type_: str
    # answer_options: list[str]
    # extra_answer_options: list[str]
    # created_by: str


@dataclass
class Answer:
    question_id: str
    left: list[str]
    right: list[str]
    created_by: str


@dataclass
class User:
    user_id: str


@dataclass
class Tag:
    name: str
    answer_id: str
    user_id: str
    value: str
