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


def bt_dang39_p3_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random đường kính bánh xe (m)
                D = random.choice([20, 24, 30, 36])
                R = Rational(D, 2)

                # Random khoảng cách từ vị trí hành khách bước lên (điểm thấp nhất M) đến mặt đất (m)
                h_min = random.choice([3, 4, 5, 6])

                # Chiều cao tâm O cách mặt đất là: R + h_min
                h_O = R + h_min

                # Số vòng quay dưới dạng hỗn số: nguyên_vong + 1/6 hoặc 1/3, 1/4 để góc alpha đẹp
                nguyen_vong = random.choice([4, 5, 6])
                phanso_vong_tu = 1
                phanso_vong_mau = random.choice([3, 4, 6])

                # Chuỗi hiển thị hỗn số cho đề bài
                hon_so_str = "%s\\frac{%s}{%s}" % (nguyen_vong, phanso_vong_tu, phanso_vong_mau)

                # Tính góc quay alpha = nguyen_vong * 2*pi + (tu/mau) * 2*pi
                alpha_chan = nguyen_vong * 2
                alpha_le = Rational(phanso_vong_tu * 2, phanso_vong_mau) * pi
                alpha_tong = alpha_chan * pi + alpha_le

                # Giá trị d = h_O + R * sin(alpha)
                # Vì sin(alpha_chan * pi + alpha_le) = sin(alpha_le)
                d_exact = h_O + R * sin(alpha_le)
                val_d = float(d_exact)

                # Làm tròn kết quả đến hàng phần mười
                kq3 = Decimal(str(val_d)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq3).replace('.', ',') + ' m'

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các phương án sai không trùng nhau
                s = []
                val_int = round(val_d, 1)
                phi_sai = [val_int + 8.6, val_int - 1.4, val_int + 1.4, val_int - 8.6, val_int + 5.5]
                for v_sai in phi_sai:
                    if v_sai > 0:
                        sai_str = str(Decimal(str(v_sai)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',') + ' m'
                        if ('$%s$' % sai_str) != da and ('$%s$' % sai_str) not in s:
                            s.append('$%s$' % sai_str)

                while len(s) < 3:
                    v_rand = round(random.uniform(10.0, 50.0), 1)
                    sai_str = str(Decimal(str(v_rand)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',') + ' m'
                    if ('$%s$' % sai_str) != da and ('$%s$' % sai_str) not in s:
                        s.append('$%s$' % sai_str)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Một vòng quay quan sát quay ngược chiều kim đồng hồ quanh trục $O$ của nó trên một mặt phẳng thẳng đứng vuông góc với mặt đất. Vòng quay có đường kính bánh xe là $%sm$ và có $12$ khoang hành khách hình trứng được thiết kế ở những vị trí trên đường tròn bánh xe sao cho khoảng cách giữa hai khoang gần nhất luôn bằng nhau. Vị trí hành khách bước lên khoang hành khách cách mặt đất $%sm$. Sau khi tất cả mọi người đã bước lên khoang hành khách, vị trí khoang hành khách của bạn A. Hỏi vị trí khoang hành khách của bạn A sau khi vòng quay quay được $%s$ vòng cách mặt đất bao nhiêu mét? Kết quả làm tròn đến hàng phần mười.'''
                                 % (latex(D), latex(h_min), hon_so_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có: $%s$ vòng tương ứng với góc quay $\\alpha = %s \\cdot 2\\pi + \\frac{%s}{%s} \\cdot 2\\pi = %s\\pi + %s$. \\\\
                             Chọn đường tròn lượng giác như hình vẽ trên. \\\\
                             Khi đó vị trí khoang hành khách của bạn A cách mặt đất là \\\\
                             $d = %s + %s \\sin \\alpha = %s + %s \\sin \\left( %s\\pi + %s \\right)$ \\\\
                             $= %s + %s \\sin \\left( %s\\pi + %s \\right) = %s + %s \\sin %s \\approx %s$. \\\\
                             Kết quả làm tròn đến hàng phần mười là %s.'''
                           % (hon_so_str, latex(nguyen_vong), latex(phanso_vong_tu), latex(phanso_vong_mau), latex(alpha_chan), latex(alpha_le),
                              latex(h_O), latex(R), latex(h_O), latex(R), latex(alpha_chan), latex(alpha_le),
                              latex(h_O), latex(R), latex(alpha_chan), latex(alpha_le), latex(h_O), latex(R), latex(alpha_le),
                              str(Decimal(str(val_d)).quantize(Decimal('0.8'), rounding=ROUND_HALF_UP)).replace('.', ','),
                              str(kq3).replace('.', ',') + ' m'))
                dapan='\\shortans[0]{$%s$}\n'%(str(kq3).replace('.', ','))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

