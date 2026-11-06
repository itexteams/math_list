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


def bt_dang17_p3_b1_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Tạo các điểm sao cho tọa độ nguyên và đẹp
                # Chọn tọa độ điểm A và đường phân giác AD là y = yA
                xa = random.randint(-2, 4)
                ya = random.randint(-2, 4)

                # Để tính toán đẹp, ta chọn delta x và delta y
                # B = (xa + dx, ya + dy)
                dx = random.choice([-2, -1, 1, 2])
                dy = random.choice([-3, -2, 2, 3])

                xb, yb = xa + dx, ya + dy

                # E là điểm đối xứng của B qua AD (y = ya)
                xe, ye = xb, 2 * ya - yb

                # Chọn tỉ số t sao cho C nằm trên đường thẳng AE: vecto AC = t * vecto AE
                # t = 2 sẽ giống bài mẫu (M nằm trên AM tạo ra phương trình c)
                t = random.choice([2, 3, -1]) 

                xc = xa + t * (xe - xa)
                yc = ya + t * (ye - ya)

                # Điểm M là trung điểm BC
                xm = Rational(xb + xc, 2)
                ym = Rational(yb + yc, 2)

                # Phương trình đường thẳng AM đi qua A(xa, ya) và M(xm, ym)
                # Vecto chỉ phương u = (xm - xa, ym - ya) -> Vecto pháp tuyến n = (-(ym-ya), xm-xa)
                n1 = -(ym - ya)
                n2 = xm - xa
                # Đưa về số nguyên tối giản
                common = gcd(int(n1*2), int(n2*2))
                a_am = int(n1 * 2 // common)
                b_am = int(n2 * 2 // common)
                c_am = -(a_am * xa + b_am * ya)

                # Đảm bảo hệ số a_am dương cho đẹp
                if a_am < 0:
                    a_am, b_am, c_am = -a_am, -b_am, -c_am

                # Chuẩn bị phương trình AM: ax + by + c = 0
                def pt_line(a, b, c):
                    res = ""
                    if a != 0:
                        res += f"{a if a != 1 else ''}x"
                    if b > 0:
                        res += f"+{b if b != 1 else ''}y"
                    elif b < 0:
                        res += f"-{abs(b) if abs(b) != 1 else ''}y"
                    if c > 0:
                        res += f"+{c}=0"
                    elif c < 0:
                        res += f"-{abs(c)}=0"
                    else:
                        res += "=0"
                    return res

                str_am = pt_line(a_am, b_am, c_am)
                str_ad = f"y - {ya} = 0" if ya != 0 else "y = 0"

                # Đáp án đúng: tung độ của C
                kq = yc

                # Các phương án nhiễu
                du = [f"${kq}$"]
                da = du[0]

                s = [f"${kq + random.randint(1, 3)}$", 
                     f"${kq - random.randint(1, 3)}$", 
                     f"${-kq}$", 
                     f"${ya + dy}$",
                     f"${ya - 2*dy}$"]

                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]
                # Tránh trùng lặp
                while das1 == da or das2 == da or das3 == da:
                    random.shuffle(s)
                    das1, das2, das3 = s[0], s[1], s[2]

                # Câu hỏi
                noidungcauhoi = (
                    "Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$. Gọi $AM, AD$ lần lượt là đường trung tuyến và đường phân giác trong của tam giác. "
                    "Các đường thẳng $AM, AD$ lần lượt có phương trình là $%s, %s$. Giả sử $B(%s;%s)$. Giá trị tung độ của điểm $C$ bằng bao nhiêu?"
                    % (str_am, str_ad, latex(xb), latex(yb))
                )


                # Lời giải chi tiết
                loigiai = (r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw [line width=1]    (141.47,51.4) -- (101.47,151.4) ;
            		\draw [line width=1]    (141.47,51.4) -- (301.47,151.4) ;
            		\draw [line width=1]    (301.47,151.4) -- (101.47,151.4) ;
            		\draw [line width=1]    (201.47,151.4) -- (141.47,51.4) ;
            		\draw [line width=1]    (141.47,51.4) -- (172.47,152.4) ;
            		\draw [line width=1]    (221.47,101.4) -- (101.47,151.4) ;
            		\draw (130,28) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\draw (82,148) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\draw (301.47,151.4) node [anchor=north west][inner sep=0.75pt]    {$C$};
            		\draw (162,154) node [anchor=north west][inner sep=0.75pt]    {$D$};
            		\draw (225,82) node [anchor=north west][inner sep=0.75pt]    {$E$};
            		\draw (196,156) node [anchor=north west][inner sep=0.75pt]    {$M$};
            	\end{tikzpicture}
            \end{center}'''
                    "Tọa độ $A$ là nghiệm của hệ: $\\begin{cases} %s \\\\ %s \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases} \\Rightarrow A(%s;%s)$. \\\\\n"
                    "Gọi $E$ là điểm đối xứng với $B$ qua $AD$ thì ta có $E \\in AC$. \\\\\n"
                    "Vì $AD: %s$ nên $E$ có tọa độ là $(%s; %s)$. \\\\\n"
                    "Đường thẳng $AC$ đi qua hai điểm $A(%s;%s)$ và $E(%s;%s)$ nên $AC$ có phương trình: "
                    % (str_ad, str_am, xa, ya, xa, ya, str_ad, xe, ye, xa, ya, xe, ye)
                )

                # Viết phương trình AC
                v_ae = (xe - xa, ye - ya)
                n_ac = (-(ye - ya), xe - xa)
                a_ac, b_ac = n_ac[0], n_ac[1]
                c_ac = -(a_ac * xa + b_ac * ya)
                str_ac = pt_line(a_ac, b_ac, c_ac)

                loigiai += (
                    "$%s$. \\\\\n"
                    "Điểm $C$ thuộc đường thẳng $AC$, $M$ là trung điểm $BC$. \\\\\n"
                    "Giả sử $C(c; %s)$ và $M\\left(\\frac{c + %s}{2}; \\frac{%s + %s}{2}\\right)$. \\\\\n"
                    "Điểm $M$ thuộc đường thẳng $AM$ nên thay tọa độ $M$ vào phương trình $%s$ ta được $c = %s$. \\\\\n"
                    "Suy ra $C(%s; %s)$. Vậy tung độ của điểm $C$ là $%s$."
                    % (str_ac, latex(simplify(Rational(-a_ac, b_ac)*symbols('c') + Rational(-c_ac, b_ac))), xb, latex(simplify(Rational(-a_ac, b_ac)*symbols('c') + Rational(-c_ac, b_ac))), yb, str_am, xc, xc, yc, yc)
                )
                dapan='\\shortans[0]{$%s$}\n'%(yc)

            # Xuất câu trắc nghiệm
            da_d = ('\\True ' + str(da))
            list_1 = [da_d, str(das1), str(das2), str(das3)]
            random.shuffle(list_1)

            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('- -', '+').replace('+ -', '-')
            return content 

