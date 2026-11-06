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


def bt_dang17_p3_b4_c4_ds10(self):
            # Khai báo biến
            # k_num / k_den: Tỉ lệ diện tích (mặc định 3/10 như đề bài để đảm bảo tính thực tế)

            lis_d = [4.8, 5.0, 5.2, 5.4, 5.6, 6.0]
            d_val = random.choice(lis_d)

            lis_p = [1200000, 1300000, 1400000, 1500000]
            p_val = random.choice(lis_p)

            k_num = 3
            k_den = 10

            # Tính toán các giá trị trung gian
            # Phương trình: (pi*x^2)/8 = (k_num/k_den) * x * sqrt(d^2 - x^2)
            # Rút gọn: (pi*x)/8 = (k_num/k_den) * sqrt(d^2 - x^2)
            # => ( (pi * k_den) / (8 * k_num) ) * x = sqrt(d^2 - x^2)
            # Đặt C = (pi * k_den) / (8 * k_num)
            c_val = (math.pi * k_den) / (8 * k_num)

            # x^2 * C^2 = d^2 - x^2 => x^2 * (C^2 + 1) = d^2 => x = sqrt(d^2 / (C^2 + 1))
            x_val = math.sqrt(d_val**2 / (c_val**2 + 1))
            x_round = round(x_val, 1)

            # Tính diện tích
            s_semi = (math.pi * x_round**2) / 8
            s_rect = x_round * math.sqrt(d_val**2 - x_round**2)
            s_total = s_semi + s_rect

            # Tính tiền (đơn vị triệu đồng)
            total_money_raw = (s_total * p_val) / 1000000
            kq_decimal = Decimal(str(total_money_raw)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            kq_final = str(kq_decimal).replace('.', ',')

            # Tạo các đáp án nhiễu
            wrong_answers = set()
            while len(wrong_answers) < 3:
                offset = random.uniform(1.5, 5.5) * random.choice([-1, 1])
                noise = round(float(kq_decimal) + offset, 1)
                noise_str = str(noise).replace('.', ',')
                if noise_str != kq_final and noise > 0:
                    wrong_answers.add('$%s$' % noise_str)

            list_ans = list(wrong_answers)
            da_d = '\\True $%s$' % kq_final
            list_ans.append(da_d)
            random.shuffle(list_ans)

            # Định dạng các số để in trong lời giải
            d_str = str(d_val).replace('.', ',')
            d2_str = str(round(d_val**2, 2)).replace('.', ',')
            p_str = str(p_val)
            x_str = str(x_round).replace('.', ',')
            s_total_str = str(round(s_total, 1)).replace('.', ',')
            c_frac_str = "\\frac{%s}{%s}" % (5, 12) if k_num == 3 and k_den == 10 else "\\frac{%s}{%s}" % (k_den, 8*k_num)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Ông An muốn làm cái cửa bằng nhôm có dạng nửa hình tròn ở phía trên và phía dưới có dạng hình chữ nhật. Biết rằng đường kính của nửa hình tròn cũng là cạnh phía trên của hình chữ nhật và đường chéo của hình chữ nhật có độ dài $%s$ mét; diện tích của nửa hình tròn bằng $\\frac{%s}{%s}$ diện tích của phần hình chữ nhật. Số tiền ông An phải trả cho biết $1m^2$ cửa có giá $%s$ đồng là bao nhiêu triệu đồng (kết quả lấy gần đúng đến hàng phần mười).'''
                             % (d_str, latex(k_num), latex(k_den), p_str))

            # Nội dung lời giải
            loigiai = ('''Gọi $x(m) (x > 0)$ là đường kính của nửa đường tròn. \\\\
            Khi đó hình chữ nhật có hai kích thước là $x$ và $\\sqrt{%s^2 - x^2}$. \\\\
            Diện tích nửa hình tròn là $\\frac{\\pi x^2}{8}$ và diện tích hình chữ nhật là $x\\sqrt{%s^2 - x^2}$. \\\\
            Theo giả thiết ta có: $\\frac{\\pi x^2}{8} = \\frac{%s}{%s}x\\sqrt{%s^2 - x^2} \\Leftrightarrow %s \\pi x = \\sqrt{%s - x^2}$ \\\\
            $\\Leftrightarrow \\frac{25}{144}\\pi^2 x^2 = %s - x^2 \\Leftrightarrow x^2\\left( \\frac{25}{144}\\pi^2 + 1 \\right) = %s \\Leftrightarrow x \\approx %s (m)$. \\\\
            Diện tích cánh cửa là: $\\frac{\\pi \\cdot %s^2}{8} + %s\\sqrt{%s^2 - %s^2} \\approx %s (m^2)$. \\\\
            Do đó số tiền ông An phải trả là: $%s \\cdot %s = %s$ (đồng). \\\\
            Vậy số tiền ông An phải trả là $%s$ triệu đồng.'''
                       % (d_str, d_str, latex(k_num), latex(k_den), d_str, c_frac_str, d2_str, d2_str, d2_str, x_str, x_str, x_str, d_str, x_str, s_total_str, p_str, s_total_str, str(int(s_total * p_val)), kq_final))
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq_final))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

