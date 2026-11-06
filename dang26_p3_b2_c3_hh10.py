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


def bt_dang26_p3_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # B3 - SUY NGHĨ TÌM CÁCH RANDOM BÀI TOÁN
            # =============================================================================
            while True:
                # Chọn tọa độ A, B, C nguyên để bài toán đẹp
                xa, ya = randint(-5, 5), randint(-5, 5)
                xb, yb = randint(-5, 5), randint(-5, 5)
                xc, yc = randint(-5, 5), randint(-5, 5)

                # Kiểm tra không thẳng hàng
                area = abs(xa*(yb - yc) + xb*(yc - ya) + xc*(ya - yb))
                # Đảm bảo G và M có tọa độ hữu tỉ đẹp (G nguyên, M là nửa nguyên)
                if area > 0 and (xa + xb + xc) % 3 == 0 and (ya + yb + yc) % 3 == 0:
                    break

            # Tính toán các thông số
            # 1. Phương trình BC
            a_bc, b_bc, c_bc = yb - yc, xc - xb, xb * yc - xc * yb
            common_bc = gcd(gcd(a_bc, b_bc), c_bc)
            line_bc = (a_bc//common_bc)*x + (b_bc//common_bc)*y + (c_bc//common_bc)

            # 2. Phương trình trung tuyến BB' (B' là trung điểm AC)
            xb_p, yb_p = Rational(xa + xc, 2), Rational(ya + yc, 2)
            a_bb, b_bb, c_bb = yb - yb_p, xb_p - xb, xb * yb_p - xb_p * yb
            # Làm đẹp hệ số BB'
            lcm_bb = sp.lcm(sp.denom(a_bb), sp.lcm(sp.denom(b_bb), sp.denom(c_bb)))
            a1, b1, c1 = int(a_bb*lcm_bb), int(b_bb*lcm_bb), int(c_bb*lcm_bb)
            com_bb = gcd(gcd(a1, b1), c1)
            a1, b1, c1 = a1//com_bb, b1//com_bb, c1//com_bb
            line_bb_expr = a1*x + b1*y + c1

            # 3. Phương trình trung tuyến CC' (C' là trung điểm AB)
            xc_p, yc_p = Rational(xa + xb, 2), Rational(ya + yb, 2)
            a_cc, b_cc, c_cc = yc - yc_p, xc_p - xc, xc * yc_p - xc_p * yc
            lcm_cc = sp.lcm(sp.denom(a_cc), sp.lcm(sp.denom(b_cc), sp.denom(c_cc)))
            a2, b2, c2 = int(a_cc*lcm_cc), int(b_cc*lcm_cc), int(c_cc*lcm_cc)
            com_cc = gcd(gcd(a2, b2), c2)
            a2, b2, c2 = a2//com_cc, b2//com_cc, c2//com_cc
            line_cc_expr = a2*x + b2*y + c2

            # Trọng tâm G và Trung điểm M của BC
            xg, yg = (xa + xb + xc) // 3, (ya + yb + yc) // 3
            xm, ym = Rational(xb + xc, 2), Rational(yb + yc, 2)
            vgm_x, vgm_y = xm - xg, ym - yg

            # =============================================================================
            # B4 - ĐIỀU CHỈNH CÁC PHƯƠNG ÁN SAI
            # =============================================================================
            da = "$A(%s; %s)$" % (xa, ya)
            s_list = []
            while len(s_list) < 3:
                dx, dy = randint(-3, 3), randint(-3, 3)
                if dx == 0 and dy == 0: continue
                fake = "$A(%s; %s)$" % (xa + dx, ya + dy)
                if fake != da and fake not in s_list:
                    s_list.append(fake)

            das1, das2, das3 = s_list[0], s_list[1], s_list[2]

            # Nội dung câu hỏi
            noidungcauhoi = (r"Trong mặt phẳng với hệ tọa độ $Oxy$, cho tam giác $ABC$ có phương trình cạnh $BC: %s = 0$, phương trình đường trung tuyến kẻ từ $B$ là $BB': %s = 0$ và phương trình đường trung tuyến kẻ từ $C$ là $CC': %s = 0$. Tọa độ đỉnh $A$ của tam giác là $(a;b)$. Tổng $a+b$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)."
                             % (latex(line_bc), latex(line_bb_expr), latex(line_cc_expr)))

            # Các đáp án
            da_d = ('\\True ' + str(da))
            list_1 = [da_d, str(das1), str(das2), str(das3)]
            random.shuffle(list_1)

            # Nội dung lời giải
            h1=xa+ya
            number = Decimal(float(h1))  # Số cần làm tròn
            kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            kqz=str(kq1).replace('.',',')

            loigiai = (r"Do $B = BB' \cap BC$ nên tọa độ điểm $B$ là nghiệm của hệ: "
                       r"$\begin{cases} %s = 0 \\ %s = 0 \end{cases} \Leftrightarrow \begin{cases} x = %s \\ y = %s \end{cases} \Rightarrow B(%s; %s)$.\\"
                       r"Tương tự $C = CC' \cap BC \Rightarrow C(%s; %s)$.\\"
                       r"Gọi $G = BB' \cap CC'$ là trọng tâm tam giác, giải hệ phương trình hai đường trung tuyến ta được $G(%s; %s)$.\\"
                       r"Gọi $M$ là trung điểm của $BC \Rightarrow M\left(%s; %s\right)$.\\"
                       r"Vì $G$ là trọng tâm nên $\overrightarrow{AM} = 3\overrightarrow{GM} \Leftrightarrow \begin{cases} %s - x_A = 3(%s) \\ %s - y_A = 3(%s) \end{cases} \Leftrightarrow \begin{cases} x_A = %s \\ y_A = %s \end{cases}$.\\"
                       r"Vậy $A(%s; %s)$. Suy ra $a+b=%s$"
                       % (latex(line_bb_expr), latex(line_bc), xb, yb, xb, yb,
                          xc, yc, xg, yg, latex(xm), latex(ym),
                          latex(xm), latex(vgm_x), latex(ym), latex(vgm_y), xa, ya, xa, ya, xa+ya))
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(kqz)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 


