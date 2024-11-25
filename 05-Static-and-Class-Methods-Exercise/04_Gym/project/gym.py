from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: [Customer]=[]
        self.trainers: [Trainer]=[]
        self.equipment: [Equipment]=[]
        self.plans:[ExercisePlan]=[]
        self.subscriptions:[Subscription]=[]

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)
    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subs=next((s for s in self.subscriptions if s.id == subscription_id), None)
        customer=next((c for c in self.customers if c.id== subs.customer_id), None)
        trainer=(next((t for t in self.trainers if t.id== subs.trainer_id), None))
        eq=next((e for e in self.equipment if e.id == subs.exercise_id), None)
        plan=next((p for p in self.plans if p.id== subs.exercise_id), None)

        return '\n'.join([subs.__repr__(), customer.__repr__(), trainer.__repr__(), eq.__repr__(), plan.__repr__()])

