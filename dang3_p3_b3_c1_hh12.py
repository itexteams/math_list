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


def bt_dang3_p3_b3_c1_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                def is_perfect_square(n):
                    """Kiểm tra xem n có phải là số chính phương hay không."""
                    return int(n**0.5)**2 == n

                def find_xyz(x_m, y_m, z_m, r):
                    """Tìm các giá trị x, y, z sao cho (x - x_m)^2 + (y - y_m)^2 + (z - z_m)^2 = r^2."""
                    attempts = 0
                    max_attempts = 10000

                    while attempts < max_attempts:
                        x = random.randint(-9, 9)
                        y = random.randint(-9, 9)
                        z = random.randint(-9, 9)

                        if (x - x_m)**2 + (y - y_m)**2 + (z - z_m)**2 == r**2:
                            return x, y, z

                        attempts += 1

                    return None  # Không tìm thấy giá trị thỏa mãn

                # Khởi tạo biến để lưu các giá trị tìm được
                x0, y0, z0 = None, None, None

                # Đếm số lần lặp
                max_attempts = 10000
                attempts = 0

                # Lặp cho đến khi tìm được x, y, z thỏa mãn điều kiện
                while attempts < max_attempts:
                    x0 = random.randint(-5, 5)
                    y0 = random.randint(-5, 5)
                    z0 = random.randint(-5, 5)

                    # Tính tổng bình phương
                    total = x0**2 + y0**2 + z0**2

                    # Kiểm tra nếu tổng bình phương là số chính phương
                    if is_perfect_square(total):
                        break

                    attempts += 1

                if attempts < max_attempts:
                    # Tìm giá trị ra sao cho ra**2 > total
                    ra, rb, rc, rd = None, None, None, None
                    for _ in range(4):
                        while True:
                            r = random.randint(1, 9)
                            if r**2 > total:
                                if ra is None:
                                    ra = r
                                elif rb is None:
                                    rb = r
                                elif rc is None:
                                    rc = r
                                elif rd is None:
                                    rd = r
                                break

                    # Khởi tạo các giá trị trung tâm
                    x_m = x0
                    y_m = y0
                    z_m = z0

                    # Tìm các giá trị xa, ya, za
                    xa, ya, za = find_xyz(x_m, y_m, z_m, ra) if ra is not None else (None, None, None)
                    xb, yb, zb = find_xyz(x_m, y_m, z_m, rb) if rb is not None else (None, None, None)
                    xc, yc, zc = find_xyz(x_m, y_m, z_m, rc) if rc is not None else (None, None, None)
                    xd, yd, zd = find_xyz(x_m, y_m, z_m, rd) if rd is not None else (None, None, None)

                a=symbols('a')
                b=symbols('b')
                c=symbols('c')
                ma=sqrt((a-xa)**2+(b-ya)**2+(c-za)**2)
                mb=sqrt((a-xb)**2+(b-yb)**2+(c-zb)**2)
                mc=sqrt((a-xc)**2+(b-yc)**2+(c-zc)**2)
                md=sqrt((a-xd)**2+(b-yd)**2+(c-zd)**2)

                ma2=((a-xa)**2+(b-ya)**2+(c-za)**2)
                mb2=((a-xb)**2+(b-yb)**2+(c-zb)**2)
                mc2=((a-xc)**2+(b-yc)**2+(c-zc)**2)
                md2=((a-xd)**2+(b-yd)**2+(c-zd)**2)

                ma1=a**2+b**2+c**2-2*a*xa-2*b*ya-2*c*za+xa**2+ya**2+za**2
                mb1=a**2+b**2+c**2-2*a*xb-2*b*yb-2*c*zb+xb**2+yb**2+zb**2
                mc1=a**2+b**2+c**2-2*a*xc-2*b*yc-2*c*zc+xc**2+yc**2+zc**2
                md1=a**2+b**2+c**2-2*a*xd-2*b*yd-2*c*zd+xd**2+yd**2+zd**2

                mab=2*a*(xb-xa)+2*b*(yb-ya)+2*c*(zb-za)
                mac=2*a*(xc-xa)+2*b*(yc-ya)+2*c*(zc-za)
                mad=2*a*(xd-xa)+2*b*(yd-ya)+2*c*(zd-za)

                vp1=ra**2-xa**2-ya**2-za**2-rb**2+xb**2+yb**2+zb**2
                vp2=ra**2-xa**2-ya**2-za**2-rc**2+xc**2+yc**2+zc**2
                vp3=ra**2-xa**2-ya**2-za**2-rd**2+xd**2+yd**2+zd**2

                om=sqrt(x_m**2+y_m**2+z_m**2)

                h1=1
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Hệ thống định vị toàn cầu GPS là một hệ thống cho phép xác định vị trí của một vật thể trong không gian. Trong cùng một thời điểm, vị trí của điểm $M$ trong không gian sẽ được xác định bởi bốn vệ tinh cho trước nhờ các bộ thu phát tín hiệu đặt trên các vệ tinh. Giả sử trong không gian với hệ tọa độ $Oxyz$, có bốn vệ tinh lần lượt đặt tại các điểm $A(%s; %s; %s), B(%s; %s; %s), C(%s; %s; %s), D(%s; %s; %s)$. Khoảng cách từ điểm $M$ đến $O$ bằng bao nhiêu? Biết vị trí $M(a;b;c)$ thỏa mãn '
                                '$MA=%s, MB=%s, MC=%s, MD=%s$. '
                                %(latex(xa),latex(ya),latex(za),
                                latex(xb),latex(yb),latex(zb),
                                latex(xc),latex(yc),latex(zc),
                                latex(xd),latex(yd),latex(zd),
                                latex(ra),latex(rb),latex(rc),latex(rd)
                                ))

                # Nội dung lời giải
                loigiai = ('Theo bài toán ta có \\\\ \n'
                        '\\hspace*{1cm} $\\heva{& MA=%s \\\\& MB=%s \\\\& MC=%s \\\\& MD=%s} \\Leftrightarrow \\heva{& %s=%s \\\\& %s=%s \\\\& %s=%s \\\\& %s=%s}$ \\\\ \n'
                        '\\hspace*{3cm} $\\Leftrightarrow \\heva{& %s=%s \\\\& %s=%s \\\\& %s=%s \\\\& %s=%s}$ \\\\ \n' 
                        '\\hspace*{3cm} $\\Leftrightarrow \\heva{& %s=%s \\\\& %s=%s \\\\& %s=%s \\\\& %s=%s}$ \\\\ \n'
                        '\\hspace*{3cm} $\\Leftrightarrow \\heva{& %s=%s \\\\& %s=%s \\\\& %s=%s}$ \\\\ \n'
                        '\\hspace*{3cm} $\\Leftrightarrow \\heva{& a=%s \\\\& b=%s \\\\& c=%s.}$ \\\\ \n'
                        'Suy ra $M(%s;%s;%s)$. \\\\ \n'
                        'Vậy $OM=\\sqrt{(%s)^2+(%s)^2+(%s)^2}=%s$.'

                        %(latex(ra),latex(rb),latex(rc),latex(rd),
                            latex(ma),latex(ra),latex(mb),latex(rb),latex(mc),latex(rc),latex(md),latex(rd),
                            latex(ma2),latex(ra**2),latex(mb2),latex(rb**2),latex(mc2),latex(rc**2),latex(md2),latex(rd**2),
                            latex(ma1),latex(ra**2),latex(mb1),latex(rb**2),latex(mc1),latex(rc**2),latex(md1),latex(rd**2),
                            latex(mab),latex(vp1),latex(mac),latex(vp2),latex(mad),latex(vp3),
                            latex(x_m),latex(y_m),latex(z_m),
                            latex(x_m),latex(y_m),latex(z_m),
                            latex(x_m),latex(y_m),latex(z_m),
                            latex(om)
                            ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(om))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

