import matplotlib.pyplot as plt
from pulp import LpMaximize, LpProblem, LpVariable, value

# 初期の価格設定
initial_price_A = 200
initial_price_B = 150
initial_price_C = 100
initial_price_D = 100

# 価格変更後の価格設定
new_price_A = 250

# 広告費の制約
ad_cost = 1000

# 各製品の生産量と利益を格納するリスト
solutions_f_A_initial = []
solutions_f_B_initial = []
solutions_f_C_initial = []
solutions_f_D_initial = []
profits_f_initial = []

solutions_f_A_new = []
solutions_f_B_new = []
solutions_f_C_new = []
solutions_f_D_new = []
profits_f_new = []

# 初期の価格設定での問題の定義
prob_initial = LpProblem("Pineapple_Company_Initial", LpMaximize)
A_initial = LpVariable('A', lowBound=0, cat='Integer')
B_initial = LpVariable('B', lowBound=0, cat='Integer')
C_initial = LpVariable('C', lowBound=0, cat='Integer')
D_initial = LpVariable('D', lowBound=0, cat='Integer')

prob_initial += initial_price_A * A_initial + initial_price_B * B_initial + initial_price_C * C_initial + initial_price_D * D_initial, "Profit"
prob_initial += 10 * A_initial + 5 * B_initial <= ad_cost, "AdCost"
prob_initial += 3 * B_initial + 8 * C_initial + 2 * D_initial <= 2000, "ProductionStaff"
prob_initial += 2 * B_initial + 2 * C_initial + 8 * D_initial <= 3000, "NewParts"
prob_initial.solve()

# 初期の利益と生産量の記録
solutions_f_A_initial.append(A_initial.varValue)
solutions_f_B_initial.append(B_initial.varValue)
solutions_f_C_initial.append(C_initial.varValue)
solutions_f_D_initial.append(D_initial.varValue)
profits_f_initial.append(value(prob_initial.objective))

# 価格変更後の問題の定義
prob_new = LpProblem("Pineapple_Company_New", LpMaximize)
A_new = LpVariable('A', lowBound=0, cat='Integer')
B_new = LpVariable('B', lowBound=0, cat='Integer')
C_new = LpVariable('C', lowBound=0, cat='Integer')
D_new = LpVariable('D', lowBound=0, cat='Integer')

prob_new += new_price_A * A_new + initial_price_B * B_new + initial_price_C * C_new + initial_price_D * D_new, "Profit"
prob_new += 10 * A_new + 5 * B_new <= ad_cost, "AdCost"
prob_new += 3 * B_new + 8 * C_new + 2 * D_new <= 2000, "ProductionStaff"
prob_new += 2 * B_new + 2 * C_new + 8 * D_new <= 3000, "NewParts"
prob_new.solve()

# 価格変更後の利益と生産量の記録
solutions_f_A_new.append(A_new.varValue)
solutions_f_B_new.append(B_new.varValue)
solutions_f_C_new.append(C_new.varValue)
solutions_f_D_new.append(D_new.varValue)
profits_f_new.append(value(prob_new.objective))

# グラフの描画
plt.figure(figsize=(12, 10))

# 利益の変化
plt.subplot(2, 1, 1)
plt.plot(["Initial Price", "New Price"], profits_f_initial + profits_f_new, marker='o', color='black', label='Profit')
plt.title('Change in profit due to price change of product A')
plt.xlabel('Pricing')
plt.ylabel('Maximum profit (dollars)')
plt.legend()
plt.grid()

# 各製品の生産量の変化
plt.subplot(2, 1, 2)
plt.plot(["Initial Price", "New Price"], solutions_f_A_initial + solutions_f_A_new, marker='o', label='A')
plt.plot(["Initial Price", "New Price"], solutions_f_B_initial + solutions_f_B_new, marker='o', label='B')
plt.plot(["Initial Price", "New Price"], solutions_f_C_initial + solutions_f_C_new, marker='o', label='C')
plt.plot(["Initial Price", "New Price"], solutions_f_D_initial + solutions_f_D_new, marker='o', label='D')
plt.xlabel('Price setting')
plt.ylabel('Production volume')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

