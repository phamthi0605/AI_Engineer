
def tinh_accuracy(so_cau_dung, tong_so_cau):
    accuracy = (so_cau_dung /tong_so_cau) * 100
    return accuracy

def dem_vat_the_hop_le(scores, nguong_tin_cay = 0.7):
    so_luong = 0
    for i in scores:
        if i >= nguong_tin_cay:
            so_luong += 1
    return so_luong


# Ex2:
so_cau_dung = tinh_accuracy(85, 100)
print(so_cau_dung)
# 85.0

# Ex4:
danh_sach_diem = [0.95, 0.42, 0.88, 0.65, 0.72, 0.30]
print(dem_vat_the_hop_le(danh_sach_diem))
# 3


