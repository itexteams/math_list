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


def bt_dang31_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # m là bán kính khoảng cách từ trục đối xứng đến giao điểm trục hoành (m > 0)
                # Trong bài gốc m = 2 => m^2 = 4 (tung độ đỉnh)
                m = random.randint(2, 5) 
                h = m**2 # Tung độ đỉnh của P1 sau khi tịnh tiến

                # x0 là hoành độ đỉnh của P1 ban đầu để tạo phương trình y = -(x-x0)^2 + h
                x0 = random.randint(1, 3)

                # Khai báo biến x cho sympy để tạo phương trình P1
                x_sym = symbols('x')
                f1_original = expand(-(x_sym - x0)**2 + h)
                f1_latex = latex(f1_original).replace('**2', '^2')

                # Tính toán các hằng số cho biểu thức T = a^3 - (2*m^2)a^2 + (3*m^4)a
                c1 = 2 * h
                c2 = 3 * (h**2)

                # Đáp số T = m^6
                kq_val = h**3
                da = '$%s$' % (kq_val)

                # Tạo các phương án sai
                s = []
                offsets = [-10, -5, 5, 10, 20, -20, 50, -50]
                random.shuffle(offsets)
                for offset in offsets:
                    val = kq_val + offset
                    if val > 0 and val != kq_val:
                        s.append('$%s$' % (val))
                    if len(s) >= 3:
                        break

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = (r'''Cho parabol $(P_1): y = %s$ cắt trục hoành tại hai điểm $A, B$ và đường thẳng $d: y = a$ ($0 < a < %s$). Xét parabol $(P_2)$ đi qua $A, B$ và có đỉnh thuộc đường thẳng $y = a$. Gọi $S_1$ là diện tích hình phẳng giới hạn bởi $(P_1)$ và $d$. Gọi $S_2$ là diện tích hình phẳng giới hạn bởi $(P_2)$ và trục hoành. Biết $S_1 = S_2$, giá trị $T = a^3 - %sa^2 + %sa$ bằng bao nhiêu?'''
                                 % (f1_latex, h, c1, c2))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Tịnh tiến sang trái x0 đơn vị: P1 thành y = -x^2 + h
                loigiai = (r'''Để việc tính toán trở nên đơn giản, ta tịnh tiến hai parabol sang trái $%s$ đơn vị. \\
                             Khi đó, phương trình các parabol mới là $(P_1): y = -x^2 + %s, (P_2): y = -\frac{a}{%s}x^2 + a$. \\
                             Gọi $A, B$ là các giao điểm của $(P_1)$ và trục $Ox \Rightarrow A(-%s;0), B(%s;0) \Rightarrow AB = %s$. \\
                             Giao điểm của $(P_1)$ và đường thẳng $d \Rightarrow M(-\sqrt{%s-a};a), N(\sqrt{%s-a};a)$. \\
                             Ta có $S_1 = 2\int_{a}^{%s} \sqrt{%s-y} \text{d}y = -\frac{4}{3}\left((%s-y)^{\frac{3}{2}}\right)\bigg|_{a}^{%s} = \frac{4}{3}(%s-a)\sqrt{%s-a}$. \\
                             $S_2 = 2\int_{0}^{%s} \left(-\frac{a}{%s}x^2 + a\right) \text{d}x = 2\left(-\frac{ax^3}{%s} + ax\right)\bigg|_{0}^{%s} = \frac{8 \cdot %s a}{3 \cdot %s} \cdot %s = \frac{8%s a}{3}$. (Tính toán diện tích Parabol $S_2 = \frac{2}{3} \cdot AB \cdot a = \frac{4}{3} \cdot %s a$). \\
                             Theo giả thiết $S_1 = S_2 \Rightarrow \frac{4}{3}(%s-a)\sqrt{%s-a} = \frac{4}{3} \cdot %s a \Rightarrow (%s-a)\sqrt{%s-a} = %s a$. \\
                             $\Leftrightarrow (%s-a)^3 = %s a^2 \Leftrightarrow %s - %sa + %sa^2 - a^3 = %s a^2$. \\
                             $\Leftrightarrow a^3 - %sa^2 + %sa = %s$. \\
                             Vậy $T = %s$.'''
                           % (latex(x0), h, latex(m**2), m, m, 2*m, 
                              h, h, 
                              h, h, h, h, h, h,
                              m, latex(m**2), latex(3*m**2), m, m, m, m, 4*m, m,
                              h, h, m, h, h, m,
                              h, latex(m**2), h**3, 3*(h**2), 3*h, latex(m**2),
                              2*h, 3*(h**2), h**3,
                              h**3))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(h**3)) 

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

