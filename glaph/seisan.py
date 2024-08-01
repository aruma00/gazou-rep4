import matplotlib.pyplot as plt
from pulp import LpMaximize, LpProblem, LpVariable, value

# 生産人員の上限を2000人から1000人まで50人ずつ減少
production_staff_range = list(range(2000, 999, -50))

# 各製品の生産量と利益を格納するリスト
solutions_f_A = []
solutions_f_B = []
solutions_f_C = []
solutions_f_D = []
profits_f = []

for staff_limit in production_staff_range:
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
    prob += 10 * A + 5 * B <= 1000, "AdCost"
    prob += 3 * B + 8 * C + 2 * D <= staff_limit, "ProductionStaff"
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
plt.figure(figsize=(10, 8))

# 利益の変化
plt.subplot(2, 1, 1)
plt.plot(production_staff_range, profits_f, marker='o', color='black', label='Profit')
plt.title('Changes in profits and optimal production volume due to an increase in production staff')
plt.xlabel('Upper limit of production staff (people)')
plt.ylabel('Maximum profit (dollars)')
plt.gca().invert_xaxis()  # x軸の逆順を設定
plt.legend()
plt.grid()

# 各製品の生産量の変化
plt.subplot(2, 1, 2)
plt.plot(production_staff_range, solutions_f_A, marker='o', label='A')
plt.plot(production_staff_range, solutions_f_B, marker='o', label='B')
plt.plot(production_staff_range, solutions_f_C, marker='o', label='C')
plt.plot(production_staff_range, solutions_f_D, marker='o', label='D')
plt.xlabel('Production staff limit (people)')
plt.ylabel('Production volume')
plt.gca().invert_xaxis()  # x軸の逆順を設定
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

