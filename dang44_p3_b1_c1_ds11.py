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


def bt_dang44_p3_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random độ dài kim giờ (R1) và kim phút (R2)
                R1 = random.randint(3, 6)
                R2 = random.randint(10, 15)

                # Số lần gặp nhau (nếu muốn random có thể chọn lần thứ 2, 3, 4)
                lan_thu = random.choice([2, 3, 4])

                # Thuật toán tính toán dựa theo lời giải mẫu:
                # Vận tốc kim giờ: w1 = 2pi / 12 = pi / 6
                # Vận tốc kim phút: w2 = 2pi / 1 = 2pi
                # Lần gặp nhau đầu tiên (sau 12 giờ) tương ứng với chu kỳ gặp nhau: T_gap = 12 / 11 giờ.
                # Vậy sau n lần gặp nhau, thời gian trôi qua là t_total = n * (12 / 11) giờ.
                t_tu = lan_thu * 12
                t_mau = 11

                # Góc quay của kim giờ: alpha_gio = w1 * t_total = (pi / 6) * (t_tu / 11)
                goc_gio_heso = Rational(t_tu, 6 * t_mau) # hệ số đi với pi

                # Góc quay của kim phút: alpha_phut = w2 * t_total = 2pi * (t_tu / 11)
                goc_phut_heso = Rational(2 * t_tu, t_mau) # hệ số đi với pi

                # Tổng quãng đường: S = R1 * alpha_gio + R2 * alpha_phut
                tong_heso = R1 * goc_gio_heso + R2 * goc_phut_heso

                # Tính giá trị xấp xỉ làm tròn đến hàng đơn vị
                val_exact = float(tong_heso * math.pi)
                kq_num = Decimal(str(val_exact)).quantize(Decimal('1.'), rounding=ROUND_HALF_UP)
                kq = str(kq_num)

                # Tạo phương án đúng
                da = '$%s\\text{ cm}$' % (kq)

                # Tạo các phương án sai ngẫu nhiên quanh đáp án đúng
                s_set = set()
                while len(s_set) < 3:
                    sai_val = int(kq_num) + random.choice([-25, -15, -10, 10, 15, 25, 40])
                    if sai_val > 0 and sai_val != int(kq_num):
                        s_set.add('$%s\\text{ cm}$' % (sai_val))

                s_list = list(s_set)
                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Câu hỏi
                noidungcauhoi = ('''Trên đồng hồ có kim chỉ giờ dài $%s\\text{ cm}$ có gắn một con rùa ở đầu kim và kim chỉ phút dài $%s\\text{ cm}$ có gắn một con thỏ ở đầu kim. Tại thời điểm quan sát đồng hồ đang chỉ thời gian lúc $12$ giờ. Hỏi khi hai kim trùng nhau lần thứ $%s$ thì tổng quãng đường đi được của rùa và thỏ là bao nhiêu? (Tính theo đơn vị cm, kết quả được làm tròn đến hàng đơn vị).'''
                                 % (latex(R1), latex(R2), latex(lan_thu)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết từng bước y như mẫu
                loigiai = ('''Vận tốc kim giờ: $\\frac{2\\pi}{12} = \\frac{\\pi}{6}$. \\\\
                           Vận tốc kim phút: $\\frac{2\\pi}{1} = 2\\pi$. \\\\
                           Gọi góc quay là $\\alpha$. \\\\
                           Thời gian kim giờ: $\\frac{\\alpha}{\\frac{\\pi}{6}} = \\frac{6\\alpha}{\\pi}$. \\\\
                           Thời gian kim phút: $\\frac{\\alpha + 2\\pi}{2\\pi}$. \\\\
                           Từ đó, ta có: $\\frac{6\\alpha}{\\pi} = \\frac{\\alpha + 2\\pi}{2\\pi} \\Rightarrow \\alpha = \\frac{\\pi}{5,5}$. \\\\
                           Thời gian gặp nhau: $\\frac{\\frac{\\pi}{5,5}}{\\frac{\\pi}{6}} = \\frac{12}{11}$ giờ. \\\\
                           Vậy sau $\\frac{%s}{11}$ giờ thì sẽ gặp nhau lần thứ %s. \\\\
                           Từ đó, kim giờ quay được 1 góc là $\\frac{%s\\pi}{11}$ và kim phút quay được 1 góc là $\\frac{%s\\pi}{11}$. \\\\
                           Vậy tổng quãng đường của rùa và thỏ đi được là $%s \\cdot \\frac{%s\\pi}{11} + %s \\cdot \\frac{%s\\pi}{11} = \\frac{%s\\pi}{11} \\approx %s\\text{cm}$.'''
                           % (latex(t_tu), latex(lan_thu),
                              latex(goc_gio_heso.p), latex(goc_phut_heso.p),
                              latex(R1), latex(goc_gio_heso.p), latex(R2), latex(goc_phut_heso.p),
                              latex(tong_heso.p), latex(kq)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

