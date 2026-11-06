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


def bt_dang16_p3_b1_c3_hh10(self):
            # Khai báo biến
            # Thay đổi hằng số trong đường thẳng d: 2x - y - k = 0 và diện tích S.
            xA, yA = 2, 2
            xB, yB = 1, 5
            # Vectơ AB = (-1, 3) => VTPT n = (3, 1). PT AB: 3(x-2) + 1(y-2) = 0 <=> 3x + y - 8 = 0

            # Để đảm bảo có nghiệm tung độ âm và một nghiệm bị loại (như mẫu), 
            # ta chọn k và S sao cho phương trình có 1 nghiệm y >= 0 và 1 nghiệm y < 0.
            # Điều kiện: 16 - 4S < 3k <= 16 + 4S
            list_k = [7, 8, 9] 
            list_S = [2, 3]
            k = random.choice(list_k)
            S = random.choice(list_S)

            # Bước 2: Tính toán chi tiết
            # Tính AB
            AB_sq = (xB - xA)**2 + (yB - yA)**2
            AB_val = sqrt(AB_sq) # sqrt(10)

            # Khoảng cách từ C đến AB: h = 2S / AB
            # h = (2*S) / sqrt(10)
            # Giả sử C(t; 2t - k) thuộc d: 2x - y - k = 0
            # d(C, AB) = |3t + (2t - k) - 8| / sqrt(3^2 + 1^2) = |5t - (k+8)| / sqrt(10)
            # => |5t - (k+8)| = 2S

            vế_phải = 2 * S
            t1_num = (k + 8) + vế_phải
            t2_num = (k + 8) - vế_phải

            # Nghiệm 1
            t1 = Rational(t1_num, 5)
            y1 = 2*t1 - k
            # Nghiệm 2
            t2 = Rational(t2_num, 5)
            y2 = 2*t2 - k

            # Lọc nghiệm có tung độ âm
            if y1 < 0:
                t_chinh = t1
                y_chinh = y1
                t_loai = t2
                y_loai = y2
            else:
                t_chinh = t2
                y_chinh = y2
                t_loai = t1
                y_loai = y1

            # Đáp án đúng (hoành độ đỉnh C)
            kq_float = float(t_chinh)
            kq_decimal = Decimal(str(kq_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            da_dung = str(kq_decimal).replace('.', ',')

            # Tạo các phương án sai
            s = []
            while len(s) < 3:
                sai = round(kq_float + random.uniform(-2, 2), 1)
                sai_str = str(sai).replace('.', ',')
                if sai_str != da_dung and sai_str not in s:
                    s.append(sai_str)

            # Bước 4: Đóng gói nội dung theo mẫu
            noidungcauhoi = (
                "Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ có $A(%s;%s), B(%s;%s)$ và đỉnh $C$ nằm trên đường thẳng $d: 2x - y - %s = 0$. "
                "Hoành độ đỉnh $C$, biết rằng $C$ có tung độ âm và diện tích tam giác $ABC$ bằng %s là bao nhiêu? (làm tròn kết quả đến hàng phần chục)."
                % (latex(xA), latex(yA), latex(xB), latex(yB), latex(k), latex(S))
            )

            loigiai = (
                "Phương trình đường thẳng $AB$ là: $\\frac{x - %s}{%s} = \\frac{y - %s}{%s} \\Leftrightarrow 3x + y - 8 = 0$. \\\\"
                "Vì $C$ nằm trên đường thẳng $d$ nên giả sử $C(t; 2t - %s)$. \\\\"
                "Ta có: $AB = \\sqrt{(%s - %s)^2 + (%s - %s)^2} = \\sqrt{10}$. \\\\"
                "Do $S_{\\triangle ABC} = %s \\Rightarrow d(C, AB) = \\frac{2 \\cdot %s}{\\sqrt{10}} = \\frac{%s}{\\sqrt{10}}$. \\\\"
                "Khi đó $\\frac{|3t + (2t - %s) - 8|}{\\sqrt{3^2 + 1^2}} = \\frac{%s}{\\sqrt{10}} \\Leftrightarrow |5t - %s| = %s$. \\\\"
                "Suy ra $t = %s$ hoặc $t = %s$. \\\\"
                "Với $t = %s$ thì $2t - %s = %s$ (loại vì $C$ có tung độ âm). \\\\"
                "Với $t = %s$ thì $2t - %s = %s$. \\\\"
                "Vậy $C\\left( %s; %s \\right) \\Rightarrow x_C = %s \\approx %s$."
                % (xA, xB-xA, yA, yB-yA, k, xB, xA, yB, yA, S, S, 2*S, k, 2*S, k+8, 2*S, 
                   latex(t_loai), latex(t_chinh), 
                   latex(t_loai), k, latex(y_loai), 
                   latex(t_chinh), k, latex(y_chinh), 
                   latex(t_chinh), latex(y_chinh), latex(t_chinh), da_dung)
            )

            # Xuất câu trắc nghiệm
            list_1 = ["\\True " + da_dung, s[0], s[1], s[2]]
            random.shuffle(list_1)

            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n" + str(noidungcauhoi) + "\n"
                "\\choice \n"
                "{" + str(list_1[0]) + "}\n"
                "{" + str(list_1[1]) + "}\n"
                "{" + str(list_1[2]) + "}\n"
                "{" + str(list_1[3]) + "}\n"
                "\\loigiai{" + str(loigiai) + "}\n"
                "\\end{ex}\n \\end{minipage} \n\n")
            return content 

