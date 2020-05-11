import sys
import math
import argparse


def count_of_months(principal, monthly, interest):
    interest = interest / 100
    i = count_i(interest)
    n = math.log((monthly / (monthly - i * principal)), (1 + i))
    n = math.ceil(n)
    years = n // 12
    months = n % 12
    overpayment = int(monthly * n - principal)
    if years == 0:
        print(f"You need {months} months to repay this credit!")
    elif months == 0:
        print(f"You need {years} years to repay this credit!")
    else:
        print(f"You need {years} years and {months} months to repay this credit!")
    print(f"Overpayment = {overpayment}")


def annuity_monthly_payment(principal, n, interest):
    interest = interest / 100
    i = count_i(interest)
    a = principal * ((i * pow((1 + i), n)) / (pow((1 + i), n) - 1))
    a = math.ceil(a)
    overpayment = int(a * n - principal)
    print(f"Your annuity payment = {a}!")
    print(f"Overpayment = {overpayment}")


def credit_principal(monthly_payment, n, interest):
    interest = interest / 100
    i = count_i(interest)
    mianownik = (i * pow((1 + i), n)) / (pow((1 + i), n) -1)
    p = ( monthly_payment / mianownik)
    p = math.floor(p)
    overpayment = int(monthly_payment * n - p)
    print(f"Your credit principal = {p}")
    print(f"Overpayment = {overpayment}")


def differentiated_payments(principal, periods, interest):
    interest = interest / 100
    i = count_i(interest)
    sum_ = 0
    for m in range(1, periods+1):
        d = math.ceil((principal / periods) + i * (principal - ((principal * (m - 1)) / periods)))
        sum_ += d
        print(f"Month {m}: paid out {d}")
    overpayment = int(sum_ - principal)
    print(f"Overpayment = {overpayment}")


def count_i(interest):
    i = (1/12) * interest
    return i


if len(sys.argv) == 5:
    parser = argparse.ArgumentParser()
    parser.add_argument('--type')
    parser.add_argument('--payment')
    parser.add_argument('--principal')
    parser.add_argument('--periods')
    parser.add_argument('--interest')
    args = parser.parse_args()
    if args.type == 'diff':
        if args.principal and args.periods and args.interest:
            principal = float(args.principal)
            periods = int(args.periods)
            interest = float(args.interest)
            differentiated_payments(principal, periods, interest)
        else:
            print("Incorrect parameters")
    elif args.type == 'annuity':
        if args.principal and args.periods and args.interest:
            principal = float(args.principal)
            periods = int(args.periods)
            interest = float(args.interest)
            annuity_monthly_payment(principal, periods, interest)
        elif args.payment and args.periods and args.interest:
            payment = float(args.payment)
            periods = int(args.periods)
            interest = float(args.interest)
            credit_principal(payment, periods, interest)
        elif args.principal and args.payment and args.interest:
            principal = float(args.principal)
            payment = float(args.payment)
            interest = float(args.interest)
            count_of_months(principal, payment, interest)
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
