def flatten_list(lst):
    """İç içe listeyi düzleştirir."""
    flat = []
    for item in lst:
        if isinstance(item, list):
            flat.extend(flatten_list(item))  # içeri girerek düzleştir
        else:
            flat.append(item)
    return flat

def reverse_list(lst):
    """Düz listeyi tersine çevirir."""
    return lst[::-1]

def flatten_and_reverse(lst):
    """Önce düzleştirir, sonra ters çevirir."""
    flat = flatten_list(lst)
    reversed_flat = reverse_list(flat)
    return reversed_flat

# Örnek kullanım:
input_data = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output = flatten_and_reverse(input_data)
print(output)
