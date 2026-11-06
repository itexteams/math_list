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


def bt_dang29_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Chọn k sao cho (2/3)*k là số nguyên để lời giải đẹp
                k_heso = random.choice([120, 150, 180, 210, 240, 300])
                hiso_nguyenham = int((2/3) * k_heso)

                # Số lượng cá thể ban đầu P(0)
                p0 = random.choice([500, 800, 1000, 1200, 1500, 2000])

                # Thời điểm t cần tính (ngày)
                t_target = random.choice([4, 5, 6, 7, 8, 9])


                kq_chinh_xac = hiso_nguyenham * t_target * math.sqrt(t_target) + p0

                # Làm tròn đến hàng trăm: Chia 100, làm tròn, rồi nhân lại 100
                kq_lam_tron = int(Decimal(kq_chinh_xac / 100).quantize(Decimal('1'), rounding=ROUND_HALF_UP)) * 100

                # B4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
                da_dung = '$%s$' % kq_lam_tron

                s = set()
                while len(s) < 3:
                    # Tạo phương án sai bằng cách thay đổi giá trị làm tròn hoặc lệch đơn vị
                    offset = random.choice([-200, -100, 100, 200, 300, -300])
                    sai_val = kq_lam_tron + offset
                    if sai_val > 0:
                        sai_str = '$%s$' % sai_val
                        if sai_str != da_dung:
                            s.add(sai_str)

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # B2: Viết lại bài toán theo mẫu code python
                # Câu hỏi
                noidungcauhoi = (r'''Một quần thể vi sinh vật có tốc độ tăng số lượng cá thể được ước lượng bởi $P'(t) = %s\sqrt{t}$ (cá thể/ngày) với $0 \le t \le 10$, trong đó $P(t)$ là số lượng cá thể vi sinh vật tại thời điểm $t$ ngày kể từ thời điểm ban đầu. Biết rằng ban đầu quần thể có $%s$ cá thể. Ước lượng số cá thể của quần thể sau $%s$ ngày kể từ thời điểm ban đầu bằng bao nhiêu? (kết quả làm tròn đến hàng trăm).'''
                                 % (latex(k_heso), latex(p0), latex(t_target)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'''$P(t) = \int P'(t) \text{d}t = \int %s\sqrt{t} \text{d} t = %s \int t^{\frac{1}{2}} \text{d} t = %s \cdot \frac{2}{3} t^{\frac{3}{2}} + C = %s t\sqrt{t} + C$. \\
                             Theo giả thiết, ta có $P(0) = %s \Rightarrow C = %s$. \\
                             Do đó $P(t) = %s t\sqrt{t} + %s$. \\
                             Số lượng cá thể sau $%s$ ngày là: \\
                             $P(%s) = %s \cdot %s \cdot \sqrt{%s} + %s \approx %s$ (cá thể).'''
                           % (latex(k_heso), latex(k_heso), latex(k_heso), latex(hiso_nguyenham),
                              latex(p0), latex(p0),
                              latex(hiso_nguyenham), latex(p0),
                              latex(t_target), latex(t_target), latex(hiso_nguyenham), latex(t_target), latex(t_target), latex(p0), latex(kq_lam_tron)))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_lam_tron))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  

