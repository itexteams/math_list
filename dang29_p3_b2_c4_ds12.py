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


def bt_dang29_p3_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo danh sách dạng
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Random số lượng bóng trong các hộp
                # Hộp 1
                w1 = randint(4, 6)   # Số bóng trắng hộp I
                r1 = randint(6, 8)   # Số bóng đỏ hộp I
                n1 = w1 + r1         # Tổng bóng hộp I

                # Hộp 2
                w2 = randint(8, 12)  # Số bóng trắng hộp II
                r2 = randint(13, 17) # Số bóng đỏ hộp II
                n2 = w2 + r2         # Tổng bóng hộp II

                # Bước 2: Tính toán các xác suất
                # Chọn 2 bóng từ hộp I: C(n1, 2)
                omega1 = Rational(n1 * (n1 - 1), 2)

                # Biến cố A: "Hai quả bóng lấy từ hộp I khác màu" (1 trắng, 1 đỏ)
                # P(A) = (w1 * r1) / C(n1, 2)
                p_A = Rational(w1 * r1, omega1)

                # Biến cố A_bar: "Hai quả bóng lấy từ hộp I cùng màu"
                # Chia thành 2 trường hợp: 2 trắng hoặc 2 đỏ
                p_2w = Rational(w1 * (w1 - 1), 2 * omega1)
                p_2r = Rational(r1 * (r1 - 1), 2 * omega1)
                p_A_bar = p_2w + p_2r

                # Biến cố B: "Quả bóng màu trắng lấy ra từ hộp II"
                # Sau khi chuyển 2 quả, tổng bóng hộp II là n2 + 2
                n2_new = n2 + 2

                # P(B|A): Lấy được 1 trắng 1 đỏ từ hộp I -> Hộp II có w2 + 1 bóng trắng
                p_B_cond_A = Rational(w2 + 1, n2_new)

                # P(B|A_bar) cần tính chi tiết từ 2w hoặc 2r
                # P(B) = P(B|A)*P(A) + P(B|2w)*P(2w) + P(B|2r)*P(2r)
                p_B = p_A * p_B_cond_A + p_2w * Rational(w2 + 2, n2_new) + p_2r * Rational(w2, n2_new)

                # Xác suất để bóng trắng lấy ra từ hộp II là bóng được chuyển từ hộp I
                # P(Chuyển từ I \cap B) = P(A)* (1/n2_new) + P(2w)* (2/n2_new)
                p_fromI_and_B = p_A * Rational(1, n2_new) + p_2w * Rational(2, n2_new)

                # Xác suất hậu nghiệm Bayes
                p_final = p_fromI_and_B / p_B

                # Rút gọn phân số a/b
                a = p_final.p
                b = p_final.q
                kq_final = a + b

                # Bước 3: Tạo các đáp án gây nhiễu
                da = '$%s$' % (latex(kq_final))
                s = [
                    '$%s$' % (latex(kq_final + 2)),
                    '$%s$' % (latex(kq_final - 2)),
                    '$%s$' % (latex(kq_final + randint(3, 5))),
                    '$%s$' % (latex(kq_final - randint(3, 5))),
                    '$%s$' % (latex(a + b + 5)),
                    '$%s$' % (latex(abs(a - b)))
                ]

                # Loại bỏ các giá trị trùng với đáp án đúng
                s = [x for x in s if x != da]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Bước 4: Nội dung câu hỏi
                noidungcauhoi = ('''Có hai chiếc hộp, hộp $I$ có $%s$ quả bóng màu trắng và $%s$ quả bóng màu đỏ, hộp $II$ có $%s$ quả bóng màu trắng và $%s$ quả bóng màu đỏ. Các quả bóng có cùng kích thước và khối lượng. Lấy ngẫu nhiên hai quả bóng từ hộp $I$ bỏ vào hộp $II$. Sau đó, lấy ra ngẫu nhiên một quả bóng từ hộp $II$. Xác suất để quả bóng được lấy ra từ hộp $II$ là quả bóng được chuyển từ hộp $I$ sang, biết rằng quả bóng đó có màu trắng là $\\frac{a}{b}$ (là phân số tối giản). Tổng $a+b$ bằng bao nhiêu?'''
                                 % (latex(w1), latex(r1), latex(w2), latex(r2)))

                # Bước 5: Nội dung lời giải chi tiết
                loigiai = ('''Gọi biến cố $A$: "Hai quả bóng lấy ra từ hộp $I$ khác màu", suy ra $\\bar{A}$: "Hai quả bóng lấy ra từ hộp $I$ cùng màu".\\\\
                             Số cách chọn $2$ quả bóng từ hộp $I$ là $C_{%s}^2 = %s$.\\\\
                             Xác suất của biến cố $A$ là: $P(A) = \\frac{%s \\cdot %s}{%s} = \\frac{%s}{%s}$.\\\\
                             Xác suất của biến cố $\\bar{A}$ gồm hai trường hợp: \\\\
                             + Lấy được $2$ bóng trắng: $P(A_{2w}) = \\frac{C_{%s}^2}{%s} = \\frac{%s}{%s}$.\\\\
                             + Lấy được $2$ bóng đỏ: $P(A_{2r}) = \\frac{C_{%s}^2}{%s} = \\frac{%s}{%s}$.\\\\
                             Suy ra $P(\\bar{A}) = P(A_{2w}) + P(A_{2r}) = \\frac{%s}{%s}$.\\\\
                             Gọi biến cố $B$: "Quả bóng màu trắng lấy ra từ hộp $II$".\\\\
                             Khi đó, theo công thức xác suất đầy đủ: \\\\
                             $P(B) = P(B|A) \\cdot P(A) + P(B|A_{2w}) \\cdot P(A_{2w}) + P(B|A_{2r}) \\cdot P(A_{2r})$\\\\
                             $P(B) = \\frac{%s+1}{%s+2} \\cdot \\frac{%s}{%s} + \\frac{%s+2}{%s+2} \\cdot \\frac{%s}{%s} + \\frac{%s}{%s+2} \\cdot \\frac{%s}{%s} = \\frac{%s}{%s}$.\\\\
                             Xác suất để quả bóng màu trắng lấy ra từ hộp $II$ là quả bóng được chuyển từ hộp $I$ là:\\\\
                             $P(I|B) = \\frac{P(B \\cap I)}{P(B)} = \\frac{P(A) \\cdot \\frac{1}{%s+2} + P(A_{2w}) \\cdot \\frac{2}{%s+2}}{P(B)} = \\frac{%s}{%s} = \\frac{%s}{%s}$.\\\\
                             Vậy $a = %s; b = %s$ và $a + b = %s$.'''
                           % (latex(n1), latex(omega1), latex(w1), latex(r1), latex(omega1), latex(p_A.p), latex(p_A.q),
                              latex(w1), latex(omega1), latex(p_2w.p), latex(p_2w.q),
                              latex(r1), latex(omega1), latex(p_2r.p), latex(p_2r.q),
                              latex(p_A_bar.p), latex(p_A_bar.q),
                              latex(w2), latex(n2), latex(p_A.p), latex(p_A.q),
                              latex(w2), latex(n2), latex(p_2w.p), latex(p_2w.q),
                              latex(w2), latex(n2), latex(p_2r.p), latex(p_2r.q),
                              latex(p_B.p), latex(p_B.q),
                              latex(n2), latex(n2), latex(p_fromI_and_B.p), latex(p_fromI_and_B.q), latex(a), latex(b),
                              latex(a), latex(b), latex(kq_final)))

                dapan=' \\shortans[0]{$%s$} '%(latex(kq_final))
                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

