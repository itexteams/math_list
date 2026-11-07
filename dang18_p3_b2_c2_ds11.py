import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang18_p3_b2_c2_ds11(self):
        # Khai báo biến
        lisdang = ['1']
        dang = random.choice(lisdang)
        
        if dang == '1':
            # --- Random hóa các biến và kiểm tra điều kiện ---
            while True:
                # Giá lúc mua (a: 300 - 1500 triệu)
                a = randint(300, 1500) 
                
                # Số năm sử dụng (n: 3 - 8 năm)
                n = randint(3, 8) 
                
                # Giá giảm mỗi năm (d: 20 - 100 triệu)
                d = randint(20, 100) 
                
                # Kết quả chuẩn: sau n năm sử dụng giá giảm đúng n lần d
                kq = a - n * d
                
                # Kiểm tra: Giá còn lại phải dương và d không chiếm quá nửa trung bình mỗi năm
                if kq > 0 and d < a / (2 * n):
                    break
            
            # Kết quả đúng dạng chuỗi
            kq_str = str(kq)
            du = ['$%s$' % (kq_str)]
            da = random.choice(du)
            
            # --- Tạo các đáp án sai ---
            # Sai lầm 1: Nhầm công thức u_n = a - (n-1)*d (chỉ giảm n-1 lần)
            # Sai lầm 2: Nhầm thành n+1 lần giảm giá
            # Sai lầm 3: Nhầm phép cộng
            s_raw = [
                a - d * (n - 1),
                a - d * (n + 1),
                a + d * n,
                kq + d,
                kq - d,
                kq + randint(1, 3) * 10,
                kq - randint(1, 3) * 10,
            ]
            
            s_formatted = []
            for val in s_raw:
                if val > 0 and val != kq:
                    s_formatted.append('$%s$' % (str(val)))
            
            # Loại bỏ trùng lặp và đảm bảo có đủ 3 đáp án sai
            s = list(set(s_formatted))
            while len(s) < 3:
                val_fake = kq + randint(4, 7) * 10
                if val_fake > 0 and str(val_fake) != kq_str:
                    s.append('$%s$' % (str(val_fake)))
                s = list(set(s))
            
            das1 = random.choice(s)
            s.remove(das1)
            das2 = random.choice(s)
            s.remove(das2)
            das3 = random.choice(s)
            
            # Câu hỏi
            noidungcauhoi = ('''Giá của một chiếc xe ô tô lúc mua mới là $%s$ triệu đồng. Cứ sau mỗi năm sử dụng, giá của chiếc xe ô tô giảm $%s$ triệu đồng. Giá còn lại của chiếc xe sau $%s$ năm sử dụng bằng bao nhiêu triệu đồng?'''
                             % (latex(a), latex(d), latex(n)))
            
            # Các đáp án trắc nghiệm
            da_d = '\\True ' + str(da)
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 
            
            # Đưa các đáp án vào danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)
            
            # Nội dung lời giải (Chuẩn logic Cấp số cộng: sau n năm tương ứng số hạng thứ n + 1)
            loigiai = ('''Gọi $u_1 = %s$ là giá trị lúc mua mới của chiếc xe.\\\\
Cứ sau mỗi năm sử dụng, giá trị xe giảm $%s$ triệu đồng nên dãy số thể hiện giá trị xe qua các năm lập thành một cấp số cộng có công sai $d = -%s$.\\\\
Giá còn lại của chiếc xe sau $%s$ năm sử dụng tương ứng với số hạng thứ $%s$ của cấp số cộng:\\\\
$u_{%s} = u_1 + %sd = %s - %s \\cdot %s = %s\\text{ (triệu đồng)}.$'''
                       % (latex(a),
                          latex(d),
                          latex(d),
                          latex(n),
                          latex(n + 1),
                          latex(n + 1),
                          latex(n),
                          latex(a),
                          latex(n),
                          latex(d),
                          latex(kq)))
            
            # Đáp án điền khuyết
            dapan = ' \\shortans[0]{$%s$} ' % (latex(kq))
        
        # Xuất câu hỏi với đáp án và lời giải vào môi trường LaTeX
        content = ('\\begin{minipage}{\\textwidth} \n'
                   '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) + '\n'
                   '\\loigiai{ \n'
                   + str(loigiai) + '}\n'
                   '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('.0', '')
        return content