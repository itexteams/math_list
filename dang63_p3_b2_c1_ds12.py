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


def bt_dang63_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khởi tạo bộ dữ liệu chuẩn tránh nghiệm lẻ xấu (N, P_m_str, P0, dP, dN, ans)
                # N: Số căn hộ
                # P_m_str: Giá thuê ban đầu (triệu) dạng chuỗi hiển thị
                # P0: Giá thuê ban đầu (nghìn đồng)
                # dP: Mức tăng giá (nghìn đồng)
                # dN: Số căn hộ trống khi tăng giá
                # ans: Đáp án doanh thu tối đa (nghìn đồng)
                configs = [
                    (50, '2', 2000, 100, 2, 2250),
                    (60, '2', 2000, 100, 2, 2500),
                    (40, '1,5', 1500, 100, 1, 2750),
                    (80, '3', 3000, 200, 2, 5500),
                    (100, '4', 4000, 200, 4, 4500),
                    (70, '2,5', 2500, 100, 2, 3000)
                ]
                N, P_m_str, P0, dP, dN, ans = random.choice(configs)

                # Tính toán các hệ số của hàm bậc hai R(x) = -A_coef*x^2 + B_coef*x + C_coef
                A_coef = dP * dN
                B_coef = dP * N - P0 * dN
                C_coef = P0 * N

                # Tính điểm x tối ưu
                x_opt = B_coef / (2 * A_coef)
                if x_opt.is_integer():
                    x_opt_str = str(int(x_opt))
                else:
                    x_opt_str = str(x_opt).replace('.', ',')

                ans_str = str(ans)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(ans_str)]
                da = random.choice(du)

                # Tạo các phương án sai ngẫu nhiên lệch khỏi đáp án đúng
                s = [
                    '$%s$'%(ans + dP),
                    '$%s$'%(ans - dP),
                    '$%s$'%(ans + 2*dP),
                    '$%s$'%(ans - 2*dP),
                    '$%s$'%(ans + 3*dP),
                    '$%s$'%(ans - 3*dP),
                    '$%s$'%(ans + 50),
                    '$%s$'%(ans - 50)
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Một công ty bất động sản có $%s$ căn hộ cho thuê. Biết rằng nếu cho thuê mỗi căn hộ với giá $%s$ triệu đồng thì mọi căn hộ đều có người thuê và cứ tăng thêm giá thuê mỗi căn hộ lên $%s$ nghìn đồng thì một tháng sẽ có $%s$ căn hộ bị bỏ trống. Hỏi muốn có doanh thu cao nhất thì công ty bất động sản phải cho thuê mỗi căn hộ bao nhiêu tiền một tháng? (đơn vị nghìn đồng).'''
                                 %(latex(N), P_m_str, latex(dP), latex(dN)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $x$ là số lần tăng giá thuê ($x \\ge 0$). \\\\
            Khi đó, giá thuê mỗi căn hộ là: $%s + %sx$ (nghìn đồng). \\\\
            Số căn hộ được cho thuê là: $%s - %sx$ (căn hộ). \\\\
            Doanh thu của công ty là: \\\\
            $R(x) = (%s + %sx)(%s - %sx) = -%sx^2 + %sx + %s$ (nghìn đồng). \\\\
            Hàm số $R(x)$ là hàm số bậc hai đạt giá trị lớn nhất tại $x = \\frac{-%s}{2 \\cdot (-%s)} = %s$. \\\\
            Vậy để có doanh thu cao nhất, công ty phải cho thuê mỗi căn hộ với giá: $%s + %s \\cdot %s = %s$ (nghìn đồng).'''
                           %(latex(P0), latex(dP),
                             latex(N), latex(dN),
                             latex(P0), latex(dP), latex(N), latex(dN), latex(A_coef), latex(B_coef), latex(C_coef),
                             latex(B_coef), latex(A_coef), x_opt_str,
                             latex(P0), latex(dP), x_opt_str, ans_str))
            dapan='\\shortans[0]{$%s$}\n'%(latex(ans_str))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

