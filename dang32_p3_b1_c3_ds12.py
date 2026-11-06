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


def bt_dang32_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['2'] # 1: Bài toán chuyển động, 2: Bài toán tăng trưởng quần thể
            dang = random.choice(lisdang)

            if dang == '2':
                # B3: Suy nghĩ tìm cách random bài toán (Câu 34)
                k = random.choice([0.1, 0.2, 0.3])
                N0 = random.choice([1000, 2000, 3000, 5000])
                t_target = random.choice([2, 3, 4])

                k_str = str(k).replace('.', ',')
                # N(t) = N0 * e^(k*t)
                res_raw = N0 * math.exp(k * t_target)
                # Làm tròn đến hàng trăm theo yêu cầu đề bài
                kq_num = int(Decimal(res_raw).quantize(Decimal('100'), rounding=ROUND_HALF_UP))

                da = '$%s$ (cá thể)' % kq_num

                # B4: Điều chỉnh các phương án sai
                s = set()
                while len(s) < 3:
                    nhieu = random.choice([kq_num + 200, kq_num - 200, kq_num + 500, int(res_raw), kq_num - 100])
                    if nhieu != kq_num and nhieu > 0:
                        s.add('$%s$ (cá thể)' % int(nhieu))
                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # B2: Viết lại bài toán
                noidungcauhoi = (r'''Giả sử tốc độ tăng trưởng của một quần thể muỗi thỏa mãn công thức $N'(t) = %sN(t), 0 \le t \le 5$, trong đó $t$ là thời gian tính theo ngày, $N(t)$ là số cá thể muỗi tại thời điểm $t$. Biết rằng ban đầu quần thể muỗi có %s cá thể. Đặt $y(t) = \ln N(t)$. Tính số lượng cá thể của quần thể muỗi sau %s ngày (kết quả làm tròn đến hàng trăm).'''
                                 % (k_str, latex(N0), latex(t_target)))

                da_d = ('\\True ' + str(da))
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                loigiai = (r'''Ta có $y'(t) = [\ln N(t)]' = \frac{N'(t)}{N(t)} = \frac{%sN(t)}{N(t)} = %s$. \\
                             Suy ra $y(t) = \int y'(t) \text{d}t = \int %s \text{d} t = %st + C$. \\
                             Do đó $\ln N(t) = %st + C \Rightarrow N(t) = e^{%st+C} = C_0 \cdot e^{%st}$. \\
                             Với $N(0) = %s \Rightarrow C_0 = %s$. Vậy $N(t) = %s \cdot e^{%st}$. \\
                             Số lượng cá thể sau %s ngày là $N(%s) = %s \cdot e^{%s \cdot %s} \approx %s$ (cá thể).'''
                           % (k_str, k_str, k_str, k_str, k_str, k_str, k_str, 
                              latex(N0), latex(N0), latex(N0), k_str,
                              latex(t_target), latex(t_target), latex(N0), k_str, latex(t_target), latex(kq_num)))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_num))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

