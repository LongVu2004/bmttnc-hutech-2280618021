from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while(1 == 1):
    print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("************************MENU************************")
    print("**  1. Nhập sinh viên.                            **")
    print("**  2. Cập nhật thông tin sinh viên bằng ID.      **")
    print("**  3. Xoá sinh viên bằng ID.                     **")
    print("**  4. Tìm kiếm sinh viên theo tên.               **")
    print("**  5. Sắp sếp sinh viên theo điểm trung bình.    **")
    print("**  6. Sắp sếp sinh viên theo tên chuyên ngành.   **")
    print("**  7. Hiển thị danh sách sinh viên.              **")
    print("**  0. Thoát.                                     **")
    print("****************************************************")

    key = int(input("Nhập tuỳ chọn: "))
    if(key == 1):
        print("\n1.Thêm sinh viên.")
        qlsv.nhapSinhVien()
        print("Thêm sinh viên thành công!")
    elif (key == 2):    
        print("\n2.Cập nhật sinh viên.")
        ID = int(input("Nhập ID sinh viên cần cập nhật: "))
        qlsv.updateSinhVien(ID)
        print("Cập nhật sinh viên thành công!")
    elif (key == 3):
        if(qlsv.SoLuongSinhVien() > 0):
            print("\n2. Cập nhật thông tin sinh viên. ")
            print("\nNhập ID: ")
            ID = int(input())
            if(qlsv.deleteById(ID)):
                print("\nSinh viên có ID = ", ID, " đã bị xoá.")
            else:
                print("\nSinh viên có ID = ", ID, " không tồn tại.")
        else:
            print("\nDanh sách sinh viên trống.")
    elif (key == 4):
        if(qlsv.SoLuongSinhVien() > 0):
            print("\n4.Tìm kiếm sinh viên theo tên.")
            print("\nNhập tên sinh viên: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sách sinh viên trống.")
    elif (key == 5):
        if(qlsv.SoLuongSinhVien() > 0):
            print("\n5.Sắp sếp sinh viên theo điểm trung bình.")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên trống.")
    elif (key == 6):
        if(qlsv.SoLuongSinhVien() > 0):
            print("\n6.Sắp sếp sinh viên theo tên chuyên ngành.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên trống.")
    elif(key == 7):
        if(qlsv.SoLuongSinhVien() > 0):
            print("\n7.Hiển thị danh sách sinh viên.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên trống.")
    elif(key == 0):
        print("\nThoát chương trình.")
        break
    else:
        print("\nKhông có chức năng này!")
        print("\nhãy chọn chức năng trong hộp menu")