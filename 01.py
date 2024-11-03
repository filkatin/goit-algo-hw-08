import heapq

def minimum_cost_to_connect_cables(cables):
    # Перетворюємо список довжин кабелів у купу
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        # Два найменших кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Витрати на їх з'єднання
        cost = first + second
        total_cost += cost
        
        # Повертаємо новий кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost


# Тестування:
cables = [4, 3, 2, 6, 15, 5]  # довжини кабелів
result = minimum_cost_to_connect_cables(cables)
print(f"Загальні витрати на з'єднання кабелів: {result}")
