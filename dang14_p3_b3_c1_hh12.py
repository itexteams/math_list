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


def bt_dang14_p3_b3_c1_hh12(self):
            # Khai báo biến
            # Chọn d là bội số của 6 để khi tính nghiệm phương trình bậc 2 luôn ra số nguyên nhân với căn 3
            d = random.choice([6, 12, 18, 24]) 
            xA = random.randint(5, 20)
            yA = random.randint(10, 30)

            # Tọa độ điểm B
            xB = xA + d
            yB = yA + d

            # Chiều cao z0 và chiều dài trục quạt h
            z0 = random.randint(25, 40) * 10
            h = random.choice([40, 50, 60, 70, 80])
            c = z0 + h

            # Tính toán các hệ số trung gian cho lời giải
            r_coef = d // 3
            R2 = (2 * d**2) // 3
            k = xA + yA + d
            a_coef = 2 * xA + d
            const_term = xA**2 + xA * d + (d**2) // 6

            mid_a = xA + d // 2
            mid_b = yA + d // 2
            coef_sqrt3 = d // 6

            # Hàm hỗ trợ ẩn số 1 khi đứng trước căn bậc 2 (ví dụ: 1\sqrt{3} -> \sqrt{3})
            def fmt_sq(val):
                return "" if val == 1 else str(val)

            c_sq = fmt_sq(coef_sqrt3)

            # Kết quả đúng của bài toán
            T_val = k + c

            # Xử lý các đáp án trắc nghiệm
            du = ['$%s$' % T_val]
            da = du[0]

            # Tạo các đáp án nhiễu
            s_pool = set()
            while len(s_pool) < 3:
                sai = T_val + random.choice([-20, -10, -5, 5, 10, 20, 30])
                if sai != T_val:
                    s_pool.add(sai)

            s_list = list(s_pool)
            random.shuffle(s_list)

            das1 = '$%s$' % s_list[0]
            das2 = '$%s$' % s_list[1]
            das3 = '$%s$' % s_list[2]

            # Trộn ngẫu nhiên 4 đáp án
            list_1 = ['\\True ' + str(da), str(das1), str(das2), str(das3)]
            random.shuffle(list_1)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong không gian với hệ trục tọa độ $Oxyz$ (đơn vị trên trục tính bằng cm), người ta lắp một chiếc quạt trần ba cách, các đầu cánh tạo thành một tam giác đều. Khi quạt quay, các đầu cánh di chuyển trên một mặt phẳng song song với $(Oxy)$. Tại một thời điểm quạt dừng quay, người ta xác định được tọa hai đầu cánh quạt là $A(%s;%s;%s)$ và $B(%s;%s;%s)$. Biết rằng điểm treo quạt $S(a;b;c)$ trên trần nhà và có hoành độ lớn hơn $%s$, trục của quạt có phương thẳng đứng và có chiều dài $%s$ cm. Giá trị biểu thức $T = a + b + c$ bằng bao nhiêu?''' 
            % (xA, yA, z0, xB, yB, z0, mid_a, h))

            # Nội dung lời giải
            loigiai = ('''Độ dài cạnh $AB = \\sqrt{(%s - %s)^2 + (%s - %s)^2} = %s\\sqrt{2}$.\\\\
            Bán kính đường tròn ngoại tiếp là: $R = IA = IB = \\frac{%s\\sqrt{2}}{\\sqrt{3}} = %s\\sqrt{6} \\Rightarrow R^2 = %s$.\\\\
            Vì trục quạt thẳng đứng, điểm treo $S(a;b;%s)$ và tâm quay $I$ sẽ có cùng hoành độ và tung độ nên tâm $I(a;b;%s)$.\\\\
            Hệ phương trình khoảng cách $\\begin{cases} IA^2 = %s \\\\\\\\ IB^2 = %s \\end{cases} \\Leftrightarrow \\begin{cases} (a - %s)^2 + (b - %s)^2 = %s \\\\\\\\ (a - %s)^2 + (b - %s)^2 = %s \\end{cases} \\Rightarrow b = %s - a$.\\\\
            Thay $b = %s - a$ vào 1 trong 2 phương trình, ta được $a^2 - %sa + %s = 0 \\Leftrightarrow \\left[ \\begin{array}{l} a = %s + %s\\sqrt{3} \\\\\\\\ a = %s - %s\\sqrt{3} \\end{array} \\right.$.\\\\
            Do $a > %s$ nên $\\begin{cases} a = %s + %s\\sqrt{3} \\\\\\\\ b = %s - %s\\sqrt{3} \\end{cases}$ nên $T = a + b + c = %s + %s\\sqrt{3} + %s - %s\\sqrt{3} + %s = %s$.'''
            % (xB, xA, yB, yA, d,
               d, r_coef, R2,
               c, z0,
               R2, R2, xA, yA, R2, xB, yB, R2, k,
               k, a_coef, const_term, mid_a, c_sq, mid_a, c_sq,
               mid_a, mid_a, c_sq, mid_b, c_sq,
               mid_a, c_sq, mid_b, c_sq, c, T_val
            ))
            dapan='\\shortans[0]{$%s$}\n'%(T_val)
            # Xuất câu trắc nghiệm theo cấu trúc chuẩn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

