from typing import Generic, TypeVar, Union
from pydantic import BaseModel, validator
from pydantic.generics import GenericModel

DataType = TypeVar('DataType')


class HttpError(BaseModel):
    code: int
    message: str


class HttpResponse(GenericModel, Generic[DataType]):
    data: Union[DataType, None] = None
    error: Union[HttpError, None] = None

    @validator('error', always=True)
    def check_consistency(cls, value, values):
        if value is not None and values['data'] is not None:
            raise ValueError('must not provide both data and error')
        if value is None and values.get('data') is None:
            raise ValueError('must provide data or error')
        return value
