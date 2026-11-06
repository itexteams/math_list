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


def bt_dang22_p4_b1_c2_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Tư duy tạo dữ liệu ngẫu nhiên hợp lý
                while True:
                    H1 = random.choice([50, 100, 150, 200])   # Hoa hồng điện thoại (nghìn đồng)
                    H2 = random.choice([250, 300, 400, 500])  # Hoa hồng laptop (nghìn đồng)
                    y_fixed = randint(3, 6)                   # Số lượng laptop đã bán

                    # Tạo đích doanh thu T (nghìn đồng) đảm bảo lớn hơn doanh thu từ laptop
                    min_T = H2 * y_fixed + 2 * H1
                    T = min_T + randint(1, 8) * 100

                    # Tính toán phân số và rút gọn hệ số giống lời giải mẫu
                    gcd_all = math.gcd(math.gcd(H1, H2), T)
                    H1_sim = H1 // gcd_all
                    H2_sim = H2 // gcd_all
                    T_sim = T // gcd_all

                    R = T - H2 * y_fixed
                    R_sim = T_sim - H2_sim * y_fixed

                    ans_exact = Rational(R_sim, H1_sim)
                    ans_val = int(math.ceil(R / H1))

                    # Giới hạn đáp án trong khoảng đẹp thực tế
                    if 4 <= ans_val <= 15:
                        break

                # Xử lý chuỗi hiển thị số tiền mục tiêu linh hoạt (triệu hoặc nghìn)
                if T % 1000 == 0:
                    str_T_de = f"{T // 1000} triệu đồng"
                else:
                    str_T_de = f"{T} nghìn đồng"

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (ans_val)]
                da = random.choice(du)

                # Tạo danh sách các đáp án sai xung quanh đáp án đúng
                s = [
                    '$%s$' % (ans_val + 1),
                    '$%s$' % (ans_val - 1),
                    '$%s$' % (ans_val + 2),
                    '$%s$' % (ans_val - 2),
                    '$%s$' % (ans_val + 3),
                ]
                s = [item for item in s if int(item.replace('$', '')) > 0]
                das1, das2, das3 = random.sample(s, 3)

                # Câu hỏi
                noidungcauhoi = ('''Anh Dũng là nhân viên bán hàng tại một cửa hàng. Anh Dũng sẽ được thưởng hoa hồng $%s$ nghìn đồng cho mỗi cái điện thoại bán được và $%s$ nghìn đồng cho mỗi cái laptop bán được. Nếu tháng này anh Dũng bán được $%s$ laptop thì để nhận được từ %s trở lên tiền hoa hồng, Tìm số lượng điện thoại tối tiểu anh Dũng cần bán.'''
                                 % (latex(H1), latex(H2), latex(y_fixed), str_T_de))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Chuỗi xấp xỉ số thập phân cho lời giải
                val_approx = round(float(ans_exact), 1)
                str_approx = str(val_approx).replace('.', ',')

                # Nội dung lời giải
                loigiai = ('''Gọi $x, y$ lần lượt là số cái điện thoại và số cái laptop anh Dũng bán được. ($x, y \\in \\mathbb{{N}}^*$) \\\\
            Theo đề bài ta có: $%sx + %sy \\ge %s \\Rightarrow %sx + %sy \\ge %s$ \\\\
            Nếu anh Dũng bán được $%s$ laptop thì $%sx + %s \\cdot %s \\ge %s \\Rightarrow x \\ge \\frac{{%s}}{{%s}} \\approx %s$. \\\\
            Vì $x$ nguyên dương nên anh Dũng cần bán tối thiểu $%s$ cái điện thoại.'''
                           % (latex(H1), latex(H2), latex(T), H1_sim, H2_sim, T_sim,
                              latex(y_fixed), H1_sim, H2_sim, latex(y_fixed), T_sim, latex(R_sim), latex(H1_sim), str_approx,
                              latex(ans_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

