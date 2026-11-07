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


def bt_dang34_p1_b2_c3_hh10(self):
                # 2. Random thông số bài toán
                r1 = random.randint(40, 60) # Bán kính bánh xe (cm)
                v1 = random.randint(60, 100) # Vận tốc vòng/phút
                t = random.randint(5, 20)    # Thời gian (phút)
                
                # 3. Tính toán các bước lời giải
                g = t * v1 * 360            # Tổng góc quay (độ)
                g1 = Rational(g, 180)       # Đổi sang radian (dạng phân số * pi)
                
                kq1 = r1 * g1               # Quãng đường tính bằng cm (dạng phân số * pi)
                # Tính giá trị xấp xỉ km
                kq_val_km = float(kq1 * pi / 100000)
                
                # Làm tròn 1 chữ số thập phân và đổi dấu chấm thành dấu phẩy
                kq3 = Decimal(str(kq_val_km)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq3).replace('.', ',')
                
                # 4. Tạo các phương án sai (không trùng đáp án đúng)
                da_dung = f"${kq_str}$"
                
                phuong_an_sai = set()
                while len(phuong_an_sai) < 3:
                    # Tạo độ lệch ngẫu nhiên từ 0.5 đến 5.0
                    sai_so = random.choice([1, 2, 3, 1.5, 2.5, -1, -2, -1.5])
                    kq_sai = Decimal(str(float(kq3) + sai_so)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    kq_sai_str = f"${str(kq_sai).replace('.', ',')}$"
                    
                    if kq_sai_str != da_dung:
                        phuong_an_sai.add(kq_sai_str)
                
                list_sai = list(phuong_an_sai)
                
                # 5. Xây dựng nội dung câu hỏi (LaTeX)
                noidungcauhoi = (r'''Một máy kéo nông nghiệp với bánh xe sau có đường kính là $%s$ cm. Xe chuyển động với vận tốc không đổi trên một đường thẳng, biết rằng vận tốc của bánh xe sau là $%s$ vòng/phút. Quãng đường (đơn vị: km) đi được của máy kéo trong $%s$ phút gần nhất với giá trị nào sau đây?'''
                                 % (latex(2 * r1), latex(v1), latex(t)))

                # Trộn các đáp án
                da_d = '\\True ' + da_dung
                list_ans = [da_d, list_sai[0], list_sai[1], list_sai[2]]
                random.shuffle(list_ans)

                # 6. Xây dựng lời giải chi tiết
                loigiai = (r'''Bán kính của bánh sau là $\frac{%s}{2} = %s$ cm. \\
Góc mà bánh xe sau quay được trong $%s$ phút là:
\[ %s \cdot %s \cdot 360^\circ = %s^\circ = %s^\circ \cdot \frac{\pi}{180} = %s\pi \text{ (rad)}. \]
Quãng đường đi được của máy kéo sau $%s$ phút là:
\[ S = R \cdot \alpha = %s \cdot %s\pi = %s\pi \text{ (cm)}. \]
Đổi đơn vị sang km:
\[ \frac{%s\pi}{100000} \approx %s \text{ km}. \]'''
                           % (latex(2 * r1), latex(r1),
                              latex(t), latex(t), latex(v1), latex(g), latex(g), latex(g1),
                              latex(t), latex(r1), latex(g1), latex(kq1),
                              latex(kq1), kq_str))

                # 7. Xuất bản nội dung theo mẫu \begin{ex}
                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                           '\\choice \n'
                           '{' + str(list_ans[0]) + '}\n'
                           '{' + str(list_ans[1]) + '}\n'
                           '{' + str(list_ans[2]) + '}\n'
                           '{' + str(list_ans[3]) + '}\n'
                           '\\loigiai{' + str(loigiai) + '}\n'
                           '\\end{ex}\n \\end{minipage} \n\n')
                return content