from pydantic import BaseModel


class ExpenseBase(BaseModel):
    amount: float
    description: str
    category: str

    class Config:
        from_attributes = True


class ExpenseCreate(ExpenseBase):
    pass


class Expense(ExpenseBase):
    id: int

    class Config:
        orm_mode = True


class BudgetBase(BaseModel):
    amount: float
    category: str

    class Config:
        from_attributes = True


class BudgetCreate(BudgetBase):
    pass


class Budget(BudgetBase):
    id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: str
    password: str


class User(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

