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


def bt_dang36_p1_b1_c3_hh10(self):
            # Khai báo biến và chọn dạng (Trục Ox hoặc Trục Oy)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước B3: Suy nghĩ tìm cách random bài toán
                # Tọa độ đỉnh A(xa; ya)
                xa = random.randint(-5, 5)
                ya = random.randint(-5, 5)

                # Tọa độ điểm thuộc đường thẳng CD: M(x0; y0)
                x0 = random.randint(-5, 5)
                y0 = random.randint(-5, 5)

                # Vectơ chỉ phương của CD: u_cd = (u1; u2)
                u1 = random.choice([x for x in range(-6, 7) if x != 0])
                u2 = random.choice([x for x in range(-6, 7) if x != 0])

                # Để tạo đáp án đúng giống mẫu (dùng vectơ đối của u_cd)
                vcp_ab_x = -u1
                vcp_ab_y = -u2

                # Hàm hỗ trợ định dạng số trong phương trình tham số
                def fmt_t(val):
                    if val == 1: return "+ t"
                    if val == -1: return "- t"
                    return ("+ " + str(val) if val > 0 else str(val)) + "t"

                def fmt_const(val):
                    return str(val) if val != 0 else ""

                # Đáp án đúng (Phương trình AB)
                da_dung_str = "\\begin{cases} x = %s %s \\\\ y = %s %s \\end{cases}" % (
                    latex(xa), fmt_t(vcp_ab_x),
                    latex(ya), fmt_t(vcp_ab_y)
                )

                # Bước B4: Điều chỉnh các phương án sai không được trùng đáp án đúng
                options_set = set()
                while len(options_set) < 3:
                    # Tạo nhiễu bằng cách đảo tọa độ hoặc đổi dấu vectơ
                    case = random.randint(1, 4)
                    if case == 1: # Đảo vị trí u1, u2
                        w1, w2 = u2, -u1
                    elif case == 2: # Giữ nguyên điểm A nhưng sai vectơ
                        w1, w2 = -u2, -u1
                    elif case == 3: # Sai tọa độ điểm đi qua (dùng tọa độ x0, y0)
                        w1, w2 = u1, u2
                    else: # Sai cả điểm và vectơ
                        w1, w2 = u1, -u2

                    opt = "\\begin{cases} x = %s %s \\\\ y = %s %s \\end{cases}" % (
                        latex(xa if case != 3 else x0), fmt_t(w1),
                        latex(ya if case != 3 else y0), fmt_t(w2)
                    )
                    if opt != da_dung_str:
                        options_set.add(opt)

                list_sai = list(options_set)

                # Câu hỏi (B2: Viết lại y hệt bài toán)
                # Định dạng phương trình CD cho đề bài
                pt_cd_de = "\\begin{cases} x = %s %s \\\\ y = %s %s \\end{cases}" % (
                    latex(x0), fmt_t(u1),
                    latex(y0), fmt_t(u2)
                )

                noidungcauhoi = ("Trong mặt phẳng với hệ tọa độ $Oxy$, cho hình bình hành $ABCD$ có đỉnh $A(%s;%s)$ và phương trình đường thẳng chứa cạnh $CD$ là $%s$. Phương trình tham số của đường thẳng chứa cạnh $AB$ là"
                                 % (latex(xa), latex(ya), pt_cd_de))

                # Các đáp án
                da_d = "\\True $" + da_dung_str + "$"
                da_s1 = "$" + list_sai[0] + "$"
                da_s2 = "$" + list_sai[1] + "$"
                da_s3 = "$" + list_sai[2] + "$"

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (B2)
                loigiai = ("Đường thẳng chứa cạnh $CD$ có vectơ chỉ phương là $\\vec{u}_{CD} = (%s; %s)$.\\\\ "
                           "Vì $ABCD$ là hình bình hành nên đường thẳng chứa cạnh $AB$ song song với đường thẳng chứa cạnh $CD$ ($AB // CD$).\\\\ "
                           "Do $AB // CD$ nên đường thẳng $AB$ nhận vectơ chỉ phương của đường thẳng $CD$ làm vectơ chỉ phương, "
                           "ta có $\\vec{u}_{AB} = \\vec{u}_{CD} = (%s; %s)$ hoặc chọn $\\vec{u}_{AB} = -\\vec{u}_{CD} = (%s; %s)$.\\\\ "
                           "Đường thẳng $AB$ đi qua điểm $A(%s; %s)$ và có vectơ chỉ phương $\\vec{u}_{AB} = (%s; %s)$.\\\\ "
                           "Vậy phương trình tham số của đường thẳng chứa cạnh $AB$ là: $%s$."
                           % (latex(u1), latex(u2), 
                              latex(u1), latex(u2),
                              latex(vcp_ab_x), latex(vcp_ab_y),
                              latex(xa), latex(ya),
                              latex(vcp_ab_x), latex(vcp_ab_y),
                              da_dung_str))

            # Xuất câu trắc nghiệm (Content không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

