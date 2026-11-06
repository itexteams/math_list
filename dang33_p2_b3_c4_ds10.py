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


def bt_dang33_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # --- BƯỚC 1: TẠO DỮ LIỆU NGẪU NHIÊN ---
            # p0: Giá vé ban đầu (đơn vị: đồng)
            p0 = random.choice([200000, 300000, 400000]) 
            # d: Mức giảm giá mỗi người (đơn vị: đồng)
            d = random.choice([2000, 4000, 5000])
            # n0: Số khách tiêu chuẩn
            n0 = 50 

            # Hàm tính doanh thu: R(x) = (n0 + x) * (p0 - d*x)
            # R(x) = -d*x^2 + (p0 - n0*d)x + n0*p0
            expr_price = p0 - d*x
            expr_revenue = (n0 + x) * (p0 - d*x)
            expr_revenue_expanded = sp.expand(expr_revenue)

            # Tính toán các giá trị đặc trưng để làm phương án đúng
            # 1. Doanh thu cực đại
            x_vertex = (p0 - n0*d) / (2*d)
            r_max = expr_revenue.subs(x, x_vertex)
            upper_bound = int(r_max + 500000) # Một con số lớn hơn doanh thu cực đại

            # 2. Bài toán chi phí (Câu d)
            # Giả sử chọn x = 8 là nghiệm lớn để không bị lỗ
            x_limit = random.choice([8, 10, 12])
            cost_val = int(expr_revenue.subs(x, x_limit))
            max_guests = n0 + x_limit

            # --- BƯỚC 2: NỘI DUNG CÂU HỎI ---
            noidungcauhoi = (r'''Một công ty du lịch thông báo giá tiền cho chuyến tham quan của một nhóm khách du lịch như sau: %s khách đầu tiên có giá là %s đồng/người. Nếu có nhiều hơn %s người đăng ký thì cứ thêm 1 người, giá vé sẽ giảm %s đồng/người cho toàn bộ hành khách. Gọi $x$ là số lượng khách từ người thứ %s trở lên ($x > 0$).''' 
                             % (n0, f"{p0:,}".replace(",", " "), n0, f"{d:,}".replace(",", " "), n0 + 1))

            ########################################################################
            # a) Nhận biết: Công thức giá vé
            da_a_d = r'\True Khi đó giá vé cho toàn bộ hành khách là $(%s - %sx)$ đồng/người' % (p0, d)
            da_a_s = r'Khi đó giá vé cho toàn bộ hành khách là $(%s - %sx)$ đồng/người' % (p0, d + 1000)
            list_a = [da_a_d, da_a_s]

            loigiai_a = (r'''Số lượng khách thực tế là $50 + x$. Vì thêm $x$ người nên giá vé mỗi người giảm đi $5000x$ đồng. Vậy giá vé mới cho mỗi hành khách là $300\,000 - 5000x$ (đồng/người).''')

            ########################################################################
            # b) Thông hiểu: Công thức doanh thu
            da_b_d = r'\True Doanh thu của công ty theo $x$ là: $R(x) = (50 + x)(300\,000 - 5000x)$'
            da_b_s = r'Doanh thu của công ty theo $x$ là: $R(x) = (50 + x)(300\,000 - 4000x)$'
            # (Lưu ý: Tôi fix cứng text theo ảnh gốc để đảm bảo tính y hệt, chỉ thay đổi logic đúng sai)
            list_b = [da_b_d, da_b_s]

            loigiai_b = (r'''Doanh thu bằng số lượng khách nhân với giá vé mỗi người. Ta có công thức doanh thu là $R(x) = (50 + x)(300\,000 - 5000x)$.''')

            ########################################################################
            # c) Vận dụng: Giá trị cực đại
            target_v = 15.5 # triệu đồng
            da_c_d = r'\True Doanh thu của công ty không thể đạt $%s$ triệu đồng' % (str(target_v)).replace('.',',')
            da_c_s = r'Doanh thu của công ty có thể đạt $%s$ triệu đồng' % (str(target_v)).replace('.',',')
            list_c = [da_c_d, da_c_s]

            loigiai_c = (r'''Xét hàm số doanh thu $R(x) = (50 + x)(300\,000 - 5000x) = -5000x^2 + 50\,000x + 15\,000\,000$. \\
            Đây là hàm bậc hai có bề lõm hướng xuống, đỉnh tại $x = \frac{-50\,000}{2 \cdot (-5000)} = 5$. \\
            Giá trị cực đại $R(5) = 15\,125\,000$ đồng (tức là $15,125$ triệu đồng). \\
            Vì $15,125 < 15,5$ nên doanh thu không thể đạt mức $15,5$ triệu đồng.''')

            ########################################################################
            # d) Vận dụng cao: Bất phương trình
            da_d_d = r'\True Biết rằng chi phí thực sự cho chuyến đi là $15\,080\,000$ đồng. Để công ty không bị lỗ thì số người của nhóm khách du lịch nhiều nhất là $58$ người'
            da_d_s = r'Biết rằng chi phí thực sự cho chuyến đi là $15\,080\,000$ đồng. Để công ty không bị lỗ thì số người của nhóm khách du lịch nhiều nhất là $60$ người'
            list_d = [da_d_d, da_d_s]

            loigiai_d = (r'''Để công ty không bị lỗ thì doanh thu phải lớn hơn hoặc bằng chi phí: \\
            $R(x) \ge 15\,080\,000 \Leftrightarrow -5000x^2 + 50\,000x + 15\,000\,000 \ge 15\,080\,000$ \\
            $\Leftrightarrow -5000x^2 + 50\,000x - 80\,000 \ge 0 \Leftrightarrow x^2 - 10x + 16 \le 0$ \\
            $\Leftrightarrow 2 \le x \le 8$. \\
            Số lượng khách tối đa là $50 + x_{max} = 50 + 8 = 58$ người.''')

            # --- BƯỚC 3: XỬ LÝ RANDOM ĐÚNG/SAI ---
            def count_true(ans_list):
                return sum('\\True' in a for a in ans_list)

            while True:
                ans_a = random.choice(list_a)
                ans_b = random.choice(list_b)
                ans_c = random.choice(list_c)
                ans_d = random.choice(list_d)

                current_answers = [ans_a, ans_b, ans_c, ans_d]
                if 1 <= count_true(current_answers) <= 3:
                    break

            # --- BƯỚC 4: XUẤT NỘI DUNG ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + loigiai_a + '\n'
                '\\item ' + loigiai_b + '\n'
                '\\item ' + loigiai_c + '\n'
                '\\item ' + loigiai_d + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

