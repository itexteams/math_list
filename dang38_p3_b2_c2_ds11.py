import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

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


def bt_dang38_p3_b2_c2_ds11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Random các số trong bài toán
        nam = random.choice([10, 12, 15, 20]) # Số năm thuê
        u1 = random.choice([8, 10, 12, 15]) # Tiền thuê quý đầu (triệu đồng)
        d1_dong = random.choice([300000, 400000, 500000, 600000]) # Mức tăng theo quý (đồng)
        d1 = Rational(d1_dong, 1000000) # Đổi ra triệu đồng (ví dụ 0,5)

        v1 = random.choice([60, 70, 80, 90]) # Tiền thuê năm đầu (triệu đồng)
        d2 = random.choice([2, 3, 4, 5]) # Mức tăng theo năm (triệu đồng)

        # Tính toán số quý và chi phí theo các phương án
        n1 = nam * 4 # Số quý
        S1 = Rational(n1, 2) * (2 * u1 + (n1 - 1) * d1) # Tổng chi phí Phương án 1

        n2 = nam # Số năm
        S2 = Rational(n2, 2) * (2 * v1 + (n2 - 1) * d2) # Tổng chi phí Phương án 2

        # Hàm chuyển đổi số sang dạng chuỗi dùng dấu phẩy cho số thập phân
        def fmt_num(num):
            val = float(num)
            if val.is_integer():
                return str(int(val))
            else:
                return str(val).replace('.', ',')

        str_S1 = fmt_num(S1)
        str_S2 = fmt_num(S2)
        str_d1 = fmt_num(d1)
        d1_dong_str = f"{d1_dong:,}".replace(',', ' ')

        # So sánh tìm phương án tối ưu
        if S1 < S2:
            pa_tot = "Phương án 1"
            chi_phi_tot = str_S1
            pa_xau = "Phương án 2"
            chi_phi_xau = str_S2
        elif S2 < S1:
            pa_tot = "Phương án 2"
            chi_phi_tot = str_S2
            pa_xau = "Phương án 1"
            chi_phi_xau = str_S1
        else:
            pa_tot = "Cả hai phương án như nhau"
            chi_phi_tot = str_S1
            pa_xau = "Phương án 1"
            chi_phi_xau = str_S2

        # Các đáp án trắc nghiệm (Không có dấu chấm ở cuối)
        if S1 != S2:
            da = "%s và %s triệu đồng" % (pa_tot, chi_phi_tot)
            das1 = "%s và %s triệu đồng" % (pa_xau, chi_phi_xau)
            das2 = "%s và %s triệu đồng" % (pa_tot, chi_phi_xau)
            das3 = "%s và %s triệu đồng" % (pa_xau, chi_phi_tot)
        else:
            da = "Cả hai phương án như nhau và %s triệu đồng" % (chi_phi_tot)
            das1 = "Phương án 1 và %s triệu đồng" % (chi_phi_tot)
            das2 = "Phương án 2 và %s triệu đồng" % (chi_phi_tot)
            das3 = "Phương án 1 và %s triệu đồng" % (fmt_num(S1 + 10))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một doanh nghiệp công nghệ khởi nghiệp (Startup) chuẩn bị mở rộng quy mô và cần thuê một mặt bằng làm trung tâm kho vận phân phối hàng hóa trong thời hạn $%s$ năm. Sau khi khảo sát, doanh nghiệp nhận được hai phương án hợp đồng từ hai đơn vị cho thuê BĐS như sau:\\\\
    - Phương án 1 (Thanh toán theo quý): Tiền thuê quý đầu tiên là $%s$ triệu đồng; từ quý thứ hai trở đi, tiền thuê mỗi quý tăng thêm $%s$ đồng so với quý trước đó.\\\\
    - Phương án 2 (Thanh toán theo năm): Tiền thuê năm đầu tiên là $%s$ triệu đồng; từ năm thứ hai trở đi, tiền thuê mỗi năm tăng thêm $%s$ triệu đồng so với năm trước đó.\\\\
    Để tối ưu hóa ngân sách, doanh nghiệp cần chọn phương án để tổng chi phí thuê mặt bằng trong $%s$ năm là thấp nhất. Số tiền chi phí thấp nhất đó bằng bao nhiêu triệu đồng?'''
                         % (latex(nam), latex(u1), d1_dong_str, latex(v1), latex(d2), latex(nam)))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        if S1 != S2:
            so_sanh_str = "$%s < %s$" % (chi_phi_tot, chi_phi_xau)
            ket_luan_str = "doanh nghiệp nên chọn %s để tổng chi phí là thấp nhất, bằng $%s$ triệu đồng" % (pa_tot, chi_phi_tot)
        else:
            so_sanh_str = "$%s = %s$" % (str_S1, str_S2)
            ket_luan_str = "hai phương án có tổng chi phí bằng nhau, bằng $%s$ triệu đồng" % (chi_phi_tot)

        loigiai = ('''Thời hạn thuê mặt bằng là $%s$ năm.\\\\
    - Phương án 1 (Thanh toán theo quý):\\\\
    Số quý thuê trong $%s$ năm là $%s \\cdot 4 = %s$ quý.\\\\
    Tiền thuê mỗi quý lập thành một cấp số cộng với số hạng đầu $u_1 = %s$, công sai $d = %s$ (triệu đồng) và số các số hạng $n = %s$.\\\\
    Tổng chi phí thuê theo Phương án 1 trong $%s$ năm là:\\\\
    $S_1 = \\frac{%s}{2} \\cdot [2 \\cdot %s + (%s - 1) \\cdot %s] = %s$ (triệu đồng).\\\\
    - Phương án 2 (Thanh toán theo năm):\\\\
    Tiền thuê mỗi năm lập thành một cấp số cộng với số hạng đầu $v_1 = %s$, công sai $d\' = %s$ (triệu đồng) và số các số hạng $n\' = %s$.\\\\
    Tổng chi phí thuê theo Phương án 2 trong $%s$ năm là:\\\\
    $S_2 = \\frac{%s}{2} \\cdot [2 \\cdot %s + (%s - 1) \\cdot %s] = %s$ (triệu đồng).\\\\
    So sánh tổng chi phí của hai phương án, ta thấy %s. Do đó, %s.'''
                   % (latex(nam), latex(nam), latex(nam), latex(n1),
                      latex(u1), str_d1, latex(n1), latex(nam),
                      latex(n1), latex(u1), latex(n1), str_d1, str_S1,
                      latex(v1), latex(d2), latex(nam), latex(nam),
                      latex(nam), latex(v1), latex(nam), latex(d2), str_S2,
                      so_sanh_str, ket_luan_str))
    dapan='\\shortans[0]{$%s$}\n'%(chi_phi_tot)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content 

