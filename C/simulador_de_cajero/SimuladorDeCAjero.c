#include <stdio.h>
#include <string.h>

void showBalance(double balance);
double deposit();
double withdraw(double balance);

int main()
{
  double balance = 0;
  int choice = 0;

  do
  {
    printf("******************\n");
    printf("Enter your choice:\n");
    printf("******************\n");

    printf("1. Show Balance\n");
    printf("2. Deposit Money\n");
    printf("3. Withdraw Money\n");
    printf("4. Exit\n");

    scanf("%d", &choice);
    getchar();

    switch (choice)
    {
    case 1:
      showBalance(balance);
      break;
    case 2:
      balance += deposit();
      showBalance(balance);
      break;
    case 3:
      balance -= withdraw(balance);
      showBalance(balance);
      break;
    case 4:
      printf("Thanks for visiting!\n");
      break;
    default:
      printf("Invelid choice!\n");
      break;
    }
  } while (choice != 4);

  return 0;
}

void showBalance(double balance)
{
  printf("Your balance is: $%.2lf\n", balance);
}

double deposit()
{
  double amount = 0;
  printf("Enter amount to be deposited: ");
  scanf("%lf", &amount);
  getchar();

  if (amount > 0)
  {
    return amount;
  }
  else
  {
    printf("That's not valid amount\n");
  }
}

double withdraw(double balance)
{
  double amount = 0;

  printf("Enter amount to be wihtdraw: \n");
  scanf("%lf", &amount);
  getchar();

  if (amount > balance)
  {
    printf("Insufficient funds\n");
    return 0;
  }
  else if (amount < 0)
  {
    printf("That's not a valid amount\n");
    return 0;
  }
  else
  {
    return amount;
  }
}
