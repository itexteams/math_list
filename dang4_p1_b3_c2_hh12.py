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


def bt_dang4_p1_b3_c2_hh12(self):
            # Khai báo biến Sympy
            x, y, z = symbols('x y z')

            # --- B3: Suy nghĩ tìm cách random bài toán ---
            # Random bộ số cho đường thẳng và mặt phẳng
            a1, b1, c1 = [randint(-6, 6) for _ in range(3)] # VTCP u
            a2, b2, c2 = [randint(-6, 6) for _ in range(3)] # Các chắn trên trục
            xa, ya, za = [randint(-6, 6) for _ in range(3)] # Điểm qua đường thẳng

            # Điều kiện để không bị mẫu bằng 0 và u khác không
            while (a1 == 0 or b1 == 0 or c1 == 0 or 
                   a2 == 0 or b2 == 0 or c2 == 0 or 
                   gcd(gcd(a1, b1), c1) != 1):
                a1, b1, c1 = [randint(-6, 6) for _ in range(3)]
                a2, b2, c2 = [randint(-6, 6) for _ in range(3)]
                xa, ya, za = [randint(-6, 6) for _ in range(3)]

            # Tìm VTPT của mặt phẳng (ABC): x/a2 + y/b2 + z/c2 = 1
            bc = abs(lcm(lcm(a2, b2), c2))
            a3 = nsimplify(bc/a2)
            b3 = nsimplify(bc/b2)
            c3 = nsimplify(bc/c2)

            pt_matphang = a3*x + b3*y + c3*z - bc

            # Tính góc
            tvh = abs(a1*a3 + b1*b3 + c1*c3)
            l1 = sqrt(a1**2 + b1**2 + c1**2)
            l2 = sqrt(a3**2 + b3**2 + c3**2)
            cos_val = nsimplify(tvh/(l1*l2))

            # Đổi sang độ và làm tròn
            goc_degrees = math.degrees(math.asin(float(cos_val)))
            kq_decimal = Decimal(str(goc_degrees)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            kq_str = str(kq_decimal).replace('.', ',')

            # --- B4: Điều chỉnh phương án sai ---
            da_dung = '$%s^\\circ$' % kq_str

            # Tạo danh sách các phương án nhiễu (không trùng đáp án đúng)
            s_nhieu = []
            while len(s_nhieu) < 3:
                sai_val = float(kq_decimal) + random.choice([-3.2, -2.1, -1.5, 1.5, 2.4, 3.7])
                sai_str = '$%s^\\circ$' % (str(round(sai_val, 1)).replace('.', ','))
                if sai_str != da_dung and sai_str not in s_nhieu:
                    s_nhieu.append(sai_str)

            # Nội dung câu hỏi
            hd, td, cd = x - xa, y - ya, z - za
            noidungcauhoi = (
                'Trong không gian $Oxyz$, cho đường thẳng $d$ có phương trình '
                '$\\dfrac{%s}{%s}=\\dfrac{%s}{%s}=\\dfrac{%s}{%s}$ và ba điểm '
                '$A(%s;0;0), B(0;%s;0), C(0;0;%s)$. Góc giữa đường thẳng $d$ và mặt phẳng $(ABC)$ '
                'bằng bao nhiêu độ? (Làm tròn kết quả đến hàng phần chục).'
                % (latex(hd), latex(a1), latex(td), latex(b1), latex(cd), latex(c1), 
                   latex(a2), latex(b2), latex(c2))
            )

            # Nội dung lời giải
            loigiai = (
                'Đường thẳng $d$ có một vectơ chỉ phương là $\\vec{u}=(%s; %s; %s)$.\\\\ \n'
                'Mặt phẳng $(ABC)$ có phương trình theo đoạn chắn là: \\\\ \n'
                '$\\dfrac{x}{%s}+\\dfrac{y}{%s}+\\dfrac{z}{%s}=1 \\Leftrightarrow %s=0$.\\\\ \n'
                'Suy ra mặt phẳng $(ABC)$ có một vectơ pháp tuyến là $\\vec{n}=(%s; %s; %s)$.\\\\ \n'
                'Gọi $\\alpha$ là góc giữa $d$ và $(ABC)$, ta có: \\\\ \n'
                '$\\sin \\alpha = \\dfrac{\\left| %s \\cdot %s + %s \\cdot %s + %s \\cdot %s \\right|}{\\sqrt{(%s)^2+(%s)^2+(%s)^2} \\cdot \\sqrt{(%s)^2+(%s)^2+(%s)^2}} = %s$.\\\\ \n'
                'Do đó $\\alpha \\approx %s^\\circ$.'
                % (latex(a1), latex(b1), latex(c1),
                   latex(a2), latex(b2), latex(c2), latex(pt_matphang),
                   latex(a3), latex(b3), latex(c3),
                   latex(a1), latex(a3), latex(b1), latex(b3), latex(c1), latex(c3),
                   latex(a1), latex(b1), latex(c1), latex(a3), latex(b3), latex(c3),
                   latex(cos_val), kq_str)
            )

            # Xáo trộn đáp án
            list_1 = ['\\True ' + da_dung, s_nhieu[0], s_nhieu[1], s_nhieu[2]]
            random.shuffle(list_1)

            # Xuất nội dung theo định dạng mẫu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n'
            ).replace('\\frac', '\\dfrac').replace('--', '+').replace('+-', '-').replace('\\Leftrightarrow 1x', '\\Leftrightarrow x').replace('\\Leftrightarrow -1x', '\\Leftrightarrow -x').replace('+1y', '+y').replace('+1z', '+z').replace('-1y', '-y').replace('-1z', '-z').replace('$1x', '$x').replace('$-1x', '$-x').replace('.', ',')

            return content

