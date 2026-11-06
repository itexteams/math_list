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


def bt_dang21_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Thông số: v0 (vận tốc đầu), h0 (độ cao đầu), t_s (thời gian cần tính)
                # g = 9.8 (m/s^2)
                v0 = random.randint(50, 120)       # Vận tốc ban đầu từ 50 đến 120 m/s
                h0 = random.randint(1, 10)         # Độ cao ban đầu từ 1 đến 10 m
                t_s = random.randint(3, 8)         # Thời gian khảo sát từ 3 đến 8 giây

                # Tính toán giá trị thực: s(t) = -4.9*t^2 + v0*t + h0
                # Tại sao là -4.9? Vì nguyên hàm của -9.8t là -4.9t^2
                val_height = -4.9 * (t_s**2) + (v0 * t_s) + h0

                # Làm tròn đến hàng phần mười (0.1)
                kq_decimal = Decimal(str(val_height)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal)

                # Đáp án đúng
                da = '$%s$ m' % kq_str

                # Bước 4: Điều chỉnh các phương án sai không trùng với đáp án đúng
                s_wrong = set()
                while len(s_wrong) < 3:
                    # Tạo các phương án nhiễu bằng cách thay đổi h0 hoặc sai lệch tính toán
                    offset = random.choice([-20.5, -10.2, 15.3, 25.8, -5.0, 30.1])
                    sai_val = float(kq_decimal) + offset
                    if sai_val > 0:
                        sai_str = str(Decimal(str(sai_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                        if sai_str != kq_str:
                            s_wrong.add('$%s$ m' % sai_str)

                list_wrong = list(s_wrong)
                das1, das2, das3 = list_wrong[0], list_wrong[1], list_wrong[2]

                # Câu hỏi (B2: Viết lại y hệt bài toán theo mẫu)
                noidungcauhoi = (r'''Một viên đạn được bắn lên trời với vận tốc là $%s$ m/s bắt đầu từ độ cao $%s$ m. Chiều cao của viên đạn sau thời gian $%s$ giây kể từ lúc bắn bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị).'''
                                 % (v0, h0, t_s))

                # Nội dung lời giải (Trình bày 2 bước tích phân như mẫu ảnh)
                loigiai = (r'''Ta có vận tốc của viên đạn tại thời điểm $t$ là \\
                             $v(t) = \int -9,8 \text{d}t = -9,8t + C_1$. \\
                             Do $v(0) = %s$ nên $v(0) = -9,8 \cdot 0 + C_1 = %s \Rightarrow C_1 = %s \Rightarrow v(t) = -9,8t + %s$. \\
                             Độ cao của viên đạn tại thời điểm $t$ là \\
                             $s(t) = \int v(t) \text{d} t = \int (-9,8t + %s) \text{d} t = -4,9t^2 + %st + C_2$. \\
                             Vì $s(0) = %s$ nên $s(0) = -4,9 \cdot 0^2 + %s \cdot 0 + C_2 = %s \Rightarrow C_2 = %s \Rightarrow s(t) = -4,9t^2 + %st + %s$. \\
                             Vậy sau khoảng thời gian %s s kể từ lúc bắn, viên đạn ở độ cao \\
                             $s(%s) = -4,9 \cdot %s^2 + %s \cdot %s + %s \approx %s$ m.'''
                           % (v0, v0, v0, v0, 
                              v0, v0, h0, v0, h0, h0, v0, h0,
                              t_s, t_s, t_s, v0, t_s, h0, kq_str))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_str))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                da_d = '\\True ' + str(da)
                list_ans = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_ans)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

