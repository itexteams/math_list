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


def bt_dang8_p3_b2_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # 1. Random các thông số sao cho đề bài đẹp
                # b là kết quả của căn bậc hai, chọn b nguyên để căn(a) = b
                b = random.randint(1, 5) 
                a = b**2

                # Random hằng số c ở nhánh dưới (ví dụ: 1/4, 1/2, 2/3...)
                list_c = [Rational(1, 2), Rational(1, 3), Rational(1, 4), Rational(2, 3), Rational(3, 4), Rational(1, 6)]
                c_val = random.choice(list_c)

                # 2. Tính toán giá trị giới hạn
                # Giới hạn phải: L1 = 1 / (2*b)
                limit_right = Rational(1, 2*b)

                # Giới hạn trái: L2 = m + c_val (tại x = 0)
                # Điều kiện: m + c_val = limit_right => m = limit_right - c_val
                m_val = limit_right - c_val
                h1=m_val
                number = Decimal(float(h1))  # Số cần làm tròn
                kqz = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq1=str(kqz).replace('.', ',')

                # 3. Tạo các đáp án
                da_dung = '$m = %s$' % latex(m_val)

                # Tạo danh sách đáp án nhiễu
                s = [
                    '$m = %s$' % latex(m_val + 1),
                    '$m = %s$' % latex(m_val - 1),
                    '$m = %s$' % latex(limit_right + c_val), # Sai dấu
                    '$m = %s$' % latex(Rational(1, b) - c_val), # Quên nhân 2 ở mẫu
                    '$m = 0$' if m_val != 0 else '$m = 1$',
                    '$m = %s$' % latex(-m_val) if m_val != 0 else '$m = -1$'
                ]

                # Chọn ngẫu nhiên 3 đáp án sai từ danh sách s
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # 4. Nội dung câu hỏi
                # Sử dụng latex() để đảm bảo phân số và căn thức hiển thị đúng
                noidungcauhoi = (r'''Cho hàm số $f(x) = \begin{cases} \frac{\sqrt{x+%s}-%s}{x} & \text{khi } x > 0 \\ mx + m + %s & \text{khi } x \le 0 \end{cases}$, với $m$ là tham số. Giá trị của $m$ để hàm số có giới hạn tại $x=0$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                                 %(latex(a), latex(b), latex(c_val)))

                # 5. Các đáp án trắc nghiệm
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_ans = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_ans)

                # 6. Nội dung lời giải (Tự động tính toán các bước)
                mau_lien_hop = b + b # Tương đương \sqrt{a} + b = 2b
                loigiai=(r'''Ta có: \\
                         $\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} \frac{\sqrt{x+%s}-%s}{x} = \lim_{x \to 0^+} \frac{(x+%s)-%s^2}{x(\sqrt{x+%s}+%s)} = \lim_{x \to 0^+} \frac{1}{\sqrt{x+%s}+%s} = \frac{1}{%s}$. \\
                         $\lim_{x \to 0^-} f(x) = \lim_{x \to 0^-} \left( mx + m + %s \right) = m + %s$. \\
                         Hàm số đã cho có giới hạn tại $x = 0$ khi và chỉ khi $\lim_{x \to 0^+} f(x) = \lim_{x \to 0^-} f(x)$: \\
                         $\Leftrightarrow \frac{1}{%s} = m + %s \Leftrightarrow m = %s \approx %s$.'''
                         %(latex(a), latex(b), latex(a), latex(b), latex(a), latex(b), latex(a), latex(b), latex(mau_lien_hop),
                           latex(c_val), latex(c_val),
                           latex(mau_lien_hop), latex(c_val), latex(m_val),str(kq1)
                          ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(str(kq1))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

