import matplotlib.pyplot as plt
from pulp import LpMaximize, LpProblem, LpVariable, value

# 広告費を1000ドルから2000ドルまで50ドルずつ増加
ad_cost_range = list(range(1000, 2050, 50))

# 各製品の生産量と利益を格納するリスト
solutions_f_A = []
solutions_f_B = []
solutions_f_C = []
solutions_f_D = []
profits_f = []

for ad_cost in ad_cost_range:
    # 問題の定義
    prob = LpProblem("Pineapple_Company", LpMaximize)

    # 変数の定義
    A = LpVariable('A', lowBound=0, cat='Integer')
    B = LpVariable('B', lowBound=0, cat='Integer')
    C = LpVariable('C', lowBound=0, cat='Integer')
    D = LpVariable('D', lowBound=0, cat='Integer')

    # 目的関数
    prob += 200 * A + 150 * B + 100 * C + 100 * D, "Profit"

    # 制約条件
    prob += 10 * A + 5 * B <= ad_cost, "AdCost"
    prob += 3 * B + 8 * C + 2 * D <= 2000, "ProductionStaff"
    prob += 2 * B + 2 * C + 8 * D <= 3000, "NewParts"

    # 問題を解く
    prob.solve()

    # 各製品の生産量と利益の記録
    solutions_f_A.append(A.varValue)
    solutions_f_B.append(B.varValue)
    solutions_f_C.append(C.varValue)
    solutions_f_D.append(D.varValue)
    profits_f.append(value(prob.objective))

# グラフの描画
plt.figure(figsize=(12, 10))

# 利益の変化
plt.subplot(2, 1, 1)
plt.plot(ad_cost_range, profits_f, marker='o', color='black', label='Profit')
plt.title('Changes in profits and optimal production due to increased advertising expenditure')
plt.xlabel('Advertising expenditure (dollars)')
plt.ylabel('Maximum profits (dollars)')
plt.legend()
plt.grid()

# 各製品の生産量の変化
plt.subplot(2, 1, 2)
plt.plot(ad_cost_range, solutions_f_A, marker='o', label='A')
plt.plot(ad_cost_range, solutions_f_B, marker='o', label='B')
plt.plot(ad_cost_range, solutions_f_C, marker='o', label='C')
plt.plot(ad_cost_range, solutions_f_D, marker='o', label='D')
plt.xlabel('Advertising expenditure (dollars)')
plt.ylabel('Production volume')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

