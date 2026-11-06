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


def bt_dang15_p3_b3_c1_hh12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các thông số (đảm bảo d_A chia hết cho 3 để số liệu tọa độ đẹp)
                v_A = random.choice([600, 720, 800, 960, 1000])
                D = random.choice([100, 120, 140, 160, 180, 200])
                K = D // 2

                t_A_float = 2.25
                t_B = 2

                # Tính quãng đường máy bay A và tham số tọa độ
                d_A = int(v_A * t_A_float)
                c_A = d_A // 3

                # Tính toán chính xác vận tốc máy bay B
                # Phương trình khoảng cách dẫn đến v_B = (d_A - K * sqrt(2)) / t_B
                v_B_approx = (d_A - K * math.sqrt(2)) / t_B
                v_B_rounded = int(Decimal(str(v_B_approx)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

                # Tạo các đáp án gây nhiễu (không trùng nhau)
                wrong_pool = set()
                # Gây nhiễu bằng dấu cộng thay vì trừ trong công thức
                wrong_pool.add(int(Decimal(str((d_A + K * math.sqrt(2)) / t_B)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)))
                wrong_pool.add(v_B_rounded + random.randint(2, 5))
                wrong_pool.add(v_B_rounded - random.randint(2, 5))
                wrong_pool.add(v_B_rounded + random.randint(10, 20))
                wrong_pool.discard(v_B_rounded)

                wrongs = list(wrong_pool)[:3]
                while len(wrongs) < 3:
                    w = v_B_rounded + random.randint(-15, 15)
                    if w != v_B_rounded and w not in wrongs:
                        wrongs.append(w)

                da = '$%s$' % (v_B_rounded)
                das1 = '$%s$' % (wrongs[0])
                das2 = '$%s$' % (wrongs[1])
                das3 = '$%s$' % (wrongs[2])

                # Câu hỏi
                noidungcauhoi = ('Trong không gian với hệ trục tọa độ $Oxyz$, đơn vị trên mỗi trục tính bằng kilomet. Một máy bay '
                                 '$A$ xuất phát từ gốc tọa độ $O(0;0;0)$ lúc 6 giờ với tốc độ không đổi là $%s$ (km/h), bay theo tia '
                                 '$OM$ hợp với các trục tọa độ các góc bằng nhau. Máy bay $B$ xuất phát tại $P(%s\\sqrt{6};0;0)$ lúc 6 '
                                 'giờ 15 phút, bay theo tia $PN$ cũng hợp với các trục tọa độ các góc bằng nhau. Tốc độ của máy '
                                 'bay $B$ để đúng 8 giờ 15 phút thì khoảng cách giữa hai máy bay bằng $%s$ km bằng bao nhiêu? '
                                 '(Kết quả làm tròn đến hàng đơn vị).' % (v_A, K, D))

                # Các đáp án
                da_d = '\\True ' + str(da)
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('Thời gian bay của máy bay $A$ là $t_A = 2,25$ (giờ)\\\\' + '\n' +
                           'Quãng đường máy bay $A$ đã bay: $d_A = %s \\cdot 2,25 = %s$ km\\\\' + '\n' +
                           'Gọi $\\vec{u}=(a;b;c)$ là một vectơ chỉ phương\\\\' + '\n' +
                           'Mặt khác ta có $\\vec{u}=(a;b;c)$ hợp với các trục tọa độ các góc bằng nhau\\\\' + '\n' +
                           'Đặt $a=\\cos \\alpha, b=\\cos \\beta, c=\\cos \\gamma$.\\\\' + '\n' +
                           'Và một tính chất bất biến trong không gian là: $\\cos^2 \\alpha + \\cos^2 \\beta + \\cos^2 \\gamma = 1 (*)$\\\\' + '\n' +
                           'Đề bài cho biết máy bay bay theo tia hợp với các trục tọa độ các góc bằng nhau.\\\\' + '\n' +
                           'Nghĩa là $\\alpha = \\beta = \\gamma \\Rightarrow \\cos \\alpha = \\cos \\beta = \\cos \\gamma$ thay vào $(*) \\Rightarrow \\cos \\alpha = \\frac{1}{\\sqrt{3}} \\Rightarrow \\vec{u} = \\left( \\frac{1}{\\sqrt{3}}; \\frac{1}{\\sqrt{3}}; \\frac{1}{\\sqrt{3}} \\right)$\\\\' + '\n' +
                           'Vậy tọa độ điểm $A$ là: $OA = %s \\cdot \\vec{u} = (%s\\sqrt{3}; %s\\sqrt{3}; %s\\sqrt{3})$\\\\' + '\n' +
                           'Thời gian bay của máy bay $B$ là $t_B = 2$ (giờ) và quãng đường máy bay $B$ đã bay: $d_B = 2 \\cdot v_B$\\\\' + '\n' +
                           'Xuất phát từ $P(%s\\sqrt{6};0;0)$ và bay theo hướng tương tự máy bay $A$:\\\\' + '\n' +
                           '$\\overrightarrow{OB} = \\overrightarrow{OP} + d_B \\cdot \\vec{u} = \\left( %s\\sqrt{6} + \\frac{2v_B}{\\sqrt{3}}; \\frac{2v_B}{\\sqrt{3}}; \\frac{2v_B}{\\sqrt{3}} \\right)$\\\\' + '\n' +
                           'Vậy $AB = \\sqrt{\\left( %s\\sqrt{6} + \\frac{2v_B}{\\sqrt{3}} - %s\\sqrt{3} \\right)^2 + \\left( \\frac{2v_B}{\\sqrt{3}} - %s\\sqrt{3} \\right)^2 + \\left( \\frac{2v_B}{\\sqrt{3}} - %s\\sqrt{3} \\right)^2} = %s \\Leftrightarrow v_B \\approx %s$ km.') % (
                               v_A, d_A, 
                               d_A, c_A, c_A, c_A,
                               K,
                               K,
                               K, c_A, c_A, c_A, D, v_B_rounded
                           )
                dapan='\\shortans[0]{$%s$}\n'%(v_B_rounded)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +dapan+
                       '\\loigiai{\n' + str(loigiai) + '\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

