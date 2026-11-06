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


def bt_dang26_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Random hằng số hấp thụ lambda (la) từ 0.010 đến 0.099
                la_val = round(random.uniform(0.015, 0.085), 3)
                # Random lượng thuốc ban đầu N0 từ 100 đến 1000 mg
                n0_val = random.randint(2, 10) * 100

                # Tính toán giá trị chu kì bán thải T = ln(2) / lambda
                kq_numeric = math.log(2) / la_val
                # Làm tròn kết quả đến 2 chữ số thập phân
                kq_str = str(round(kq_numeric, 2)).replace('.', ',')

                # B4: Điều chỉnh các phương án sai (đảm bảo không trùng đáp án đúng)
                # Tạo các đáp án nhiễu dựa trên các lỗi logic phổ biến (nhầm ln(3), nhầm công thức)
                s_values = [
                    round(math.log(3) / la_val, 2),
                    round(1 / la_val, 2),
                    round(2 / la_val, 2),
                    round(math.log(2) / (la_val * 2), 2),
                    round(kq_numeric + random.uniform(2.5, 5.5), 2),
                    round(kq_numeric - random.uniform(2.5, 5.5), 2)
                ]

                # Loại bỏ giá trị trùng với đáp án đúng (nếu có)
                s_values = [v for v in s_values if round(v, 2) != round(kq_numeric, 2)]
                random.shuffle(s_values)

                # Lấy 3 đáp án sai
                das1 = str(s_values[0]).replace('.', ',')
                das2 = str(s_values[1]).replace('.', ',')
                das3 = str(s_values[2]).replace('.', ',')

                # B2: Viết lại nội dung bài toán (Câu hỏi)
                noidungcauhoi = (r'''Trong dược học, chu kì bán thải $T_{\frac{1}{2}}$ của thuốc được cơ thể hấp thụ là thời gian để lượng thuốc giảm đi một nửa so với ban đầu. Giả sử tốc độ chuyển hóa thuốc của một bệnh nhân được cho bởi hàm số $N'(t) = -%s \cdot %s \cdot e^{-%s t}$, trong đó $N_0 = %s$ mg là lượng thuốc ban đầu tại $t = 0$ và $\lambda = %s$ là hằng số hấp thụ. Hãy tính chu kì bán thải $T_{\frac{1}{2}}$ của loại thuốc này (làm tròn kết quả đến hàng phần trăm).'''
                                 % (latex(la_val), latex(n0_val), latex(la_val), latex(n0_val), latex(la_val)))

                # Đáp án đúng
                da_d = r'\True $%s$' % kq_str
                da_s1 = '$%s$' % das1
                da_s2 = '$%s$' % das2
                da_s3 = '$%s$' % das3

                # Đưa các đáp án vào danh sách và trộn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # B2: Viết lại nội dung lời giải
                loigiai = (r'''Lượng thuốc tại thời điểm $t$ là: \\ 
                           $N(t) = \int (-%s \cdot %s \cdot e^{-%s t}) \text{d}t = %s \cdot e^{-%s t} + C$. \\
                           Vì tại $t=0$, lượng thuốc là $N(0) = %s$ nên: \\
                           $%s \cdot e^{0} + C = %s \Rightarrow C = 0$. \\
                           Vậy $N(t) = %s \cdot e^{-%s t}$. \\
                           Khi $t = T_{\frac{1}{2}}$, lượng thuốc giảm còn một nửa: \\
                           $N(T_{\frac{1}{2}}) = \frac{N_0}{2} \Leftrightarrow %s \cdot e^{-%s \cdot T_{\frac{1}{2}}} = \frac{%s}{2} = %s$. \\
                           $\Leftrightarrow e^{-%s \cdot T_{\frac{1}{2}}} = \frac{1}{2} \Leftrightarrow -%s \cdot T_{\frac{1}{2}} = \ln\left(\frac{1}{2}\right) = -\ln 2$. \\
                           $\Leftrightarrow T_{\frac{1}{2}} = \frac{\ln 2}{%s} \approx %s$.'''
                           % (latex(la_val), latex(n0_val), latex(la_val), latex(n0_val), latex(la_val),
                              latex(n0_val), latex(n0_val), latex(n0_val), latex(n0_val), latex(la_val),
                              latex(n0_val), latex(la_val), latex(n0_val), latex(n0_val//2),
                              latex(la_val), latex(la_val), latex(la_val), kq_str))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

