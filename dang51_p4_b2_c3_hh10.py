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


def bt_dang51_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khi đó, kết quả B(3,3) cũng sẽ tịnh tiến tương ứng thành (3+dx, 3+dy).

            dx = random.randint(-5, 5)
            dy = random.randint(-5, 5)

            # Tọa độ các điểm mới
            xa, ya = 1 + dx, 1 + dy
            xm, ym = 4 + dx, 2 + dy

            # Các thông số tính toán (giữ nguyên tỉ lệ từ bài gốc)
            # AB = d(A, BC), BC = 2*d(M, AB)
            # Dẫn đến phương trình: |a(ym-ya) - b(xm-xa)| = 2|a(xm-xa) + b(ym-ya)|
            # Với xa=1, ya=1, xm=4, ym=2 -> |a - 3b| = 2|3a + b|
            delta_x = xm - xa
            delta_y = ym - ya

            # Trường hợp 1: b = -a (Chọn a=1, b=-1)
            a1, b1 = 1, -1
            # Đường AB: a1(x-xa) + b1(y-ya) = 0
            # Đường BC: b1(x-xm) - a1(y-ym) = 0
            # Giải hệ tìm B_chinh_xac (3+dx, 3+dy)
            xb1, yb1 = 3 + dx, 3 + dy
            kq_dung = '(%s;%s)' % (xb1, yb1)

            # Trường hợp 2: b = 7a (Chọn a=1, b=7)
            a2, b2 = 1, 7
            # Tọa độ B thứ hai (thường là phân số)
            xb2_num = b2*xm - a2*ym + a2*ya + b2*xa
            xb2_den = a2**2 + b2**2
            yb2_num = -a2*xm - b2*ym + b2*ya - a2*xa # Biến đổi từ hệ phương trình
            # Tính toán tọa độ phân số cho B2
            xb2 = Rational(19 + 5*dx, 5) # Dựa trên kết quả bài gốc 19/5 tịnh tiến
            yb2 = Rational(3 + 5*dy, 5)
            kq_loai = '(%s;%s)' % (latex(xb2), latex(yb2))

            # Bước 4: Điều chỉnh các phương án sai
            def generate_wrong_answer():
                while True:
                    w_x = xb1 + random.randint(-3, 3)
                    w_y = yb1 + random.randint(-3, 3)
                    ans = '(%s;%s)' % (w_x, w_y)
                    if ans != kq_dung:
                        return ans

            da_s1 = generate_wrong_answer()
            da_s2 = generate_wrong_answer()
            while da_s2 == da_s1: da_s2 = generate_wrong_answer()
            da_s3 = generate_wrong_answer()
            while da_s3 == da_s1 or da_s3 == da_s2: da_s3 = generate_wrong_answer()

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong mặt phẳng với hệ tọa độ $Oxy$, cho hình vuông $ABCD$ có $A(%s;%s)$ và $M(%s;%s)$ là trung điểm cạnh $BC$. Biết $B$ có tọa độ nguyên, tìm tọa độ điểm $B$.'''
                            % (latex(xa), latex(ya), latex(xm), latex(ym)))

            # Các đáp án
            da_d = ('\\True $%s$' % kq_dung)
            list_1 = [da_d, '$%s$' % da_s1, '$%s$' % da_s2, '$%s$' % da_s3]
            random.shuffle(list_1)

            # Lời giải chi tiết theo mẫu ảnh
            loigiai = ('''Giả sử $\\vec{n}_{AB} = (a;b)$ với $a^2+b^2 \\neq 0$ là vectơ pháp tuyến của đường thẳng $AB$. Suy ra đường thẳng $BC$ có vectơ pháp tuyến $\\vec{n}_{BC} = (b;-a)$. \\\\
            Đường thẳng $AB$ đi qua $A(%s;%s)$ và có vectơ pháp tuyến $\\vec{n}_{AB} = (a;b)$ nên \\\\
            $AB: a(x-%s) + b(y-%s) = 0$ hay $ax+by-%s a-%s b = 0$. \\\\
            Đường thẳng $BC$ đi qua $M(%s;%s)$ và có vectơ pháp tuyến $\\vec{n}_{BC} = (b;-a)$ nên \\\\
            $BC: b(x-%s) - a(y-%s) = 0$ hay $bx-ay+%s a-%s b = 0$. \\\\
            Ta có $AB = d(A, BC) = \\frac{|%s a - %s b|}{\\sqrt{a^2+b^2}}$ và $BC = 2d(M, AB) = 2 \\frac{|%s a + %s b|}{\\sqrt{a^2+b^2}}$. \\\\
            Vì là hình vuông nên $AB = BC \\Leftrightarrow |%s a - %s b| = 2|%s a + %s b| \\Leftrightarrow \\left[\\begin{aligned} & b = -a \\\\ & b = 7a \\end{aligned}\\right.$. \\\\
            Với $b = -a$ chọn $a=1$ suy ra $b=-1$. Ta được $AB: x-y+%s=0$ và $BC: x+y-%s=0$. \\\\
            Tọa độ điểm $B$ là nghiệm của hệ $\\begin{cases} x-y+%s=0 \\\\ x+y-%s=0 \\end{cases} \\Rightarrow B(%s;%s)$. \\\\
            Với $b = 7a$ chọn $a=1$ suy ra $b=7$. Ta được $AB: x+7y-%s=0$ và $BC: 7x-y-%s=0$. \\\\
            Tọa độ điểm $B$ là nghiệm của hệ $\\begin{cases} x+7y-%s=0 \\\\ 7x-y-%s=0 \\end{cases} \\Rightarrow B\\left(\\frac{%s}{5}; \\frac{%s}{5}\\right)$. \\\\
            Vì $B$ có tọa độ nguyên nên $B(%s;%s)$.'''
                        % (latex(xa), latex(ya), latex(xa), latex(ya), latex(xa), latex(ya),
                           latex(xm), latex(ym), latex(xm), latex(ym), latex(ym), latex(xm),
                           # Phần d(A,BC) và d(M,AB)
                           latex(delta_y), latex(delta_x), latex(delta_x), latex(delta_y),
                           latex(delta_y), latex(delta_x), latex(delta_x), latex(delta_y),
                           # Hệ 1
                           latex(ya-xa), latex(xa+ya+2*delta_y), 
                           latex(ya-xa), latex(xa+ya+2*delta_y),
                           latex(xb1), latex(yb1),
                           # Hệ 2 (Dựa trên thông số tịnh tiến từ bài gốc)
                           latex(7*ya+xa), latex(7*xm-ym),
                           latex(7*ya+xa), latex(7*xm-ym),
                           latex(19+5*dx), latex(3+5*dy),
                           # Kết luận
                           latex(xb1), latex(yb1)
                           ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

