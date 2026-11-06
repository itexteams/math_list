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


def bt_dang20_p1_b2_c6_ds10(self):
            #Khai báo biến
            # Tập A sẽ bắt đầu từ 2 và kết thúc ở n_max (n_max từ 8 đến 10 để đảm bảo đủ số lượng chữ số)
            n_max = random.randint(8, 10)
            A_list = list(range(2, n_max + 1))
            A_str = "{" + "; ".join(map(str, A_list)) + "}"

            # Phân loại chữ số chẵn và lẻ trong tập A
            chan = [x for x in A_list if x % 2 == 0]
            le = [x for x in A_list if x % 2 != 0]

            n_chan = len(chan)
            n_le = len(le)
            n_total = len(A_list)

            # Bước tính toán toán học
            # 1. Số phần tử của không gian mẫu n(Omega) = A(n_total, 4)
            omega = factorial(n_total) // factorial(n_total - 4)

            # 2. Số cách chọn 2 chữ số chẵn và 2 chữ số lẻ
            cach_chon_chan = binomial(n_chan, 2)
            cach_chon_le = binomial(n_le, 2)

            # 3. Số cách sắp xếp 4 chữ số đã chọn (hoán vị)
            hoan_vi = factorial(4)

            # 4. Số phần tử của biến cố X: n(A) = C(n_chan, 2) * C(n_le, 2) * 4!
            na = cach_chon_chan * cach_chon_le * hoan_vi

            # 5. Xác suất
            xac_suat = Rational(na, omega)

            # B4: Điều chỉnh các phương án sai (đảm bảo không trùng đáp án đúng)
            def generate_distractors(correct_rational):
                s = set()
                while len(s) < 3:
                    # Tạo các phân số lân cận hoặc ngẫu nhiên
                    num = correct_rational.p + random.randint(-5, 5)
                    den = correct_rational.q + random.randint(-5, 5)
                    if num > 0 and den > 0 and num < den:
                        f = Rational(num, den)
                        if f != correct_rational:
                            s.add("$%s$" % latex(f))
                return list(s)

            distractors = generate_distractors(xac_suat)
            da_dung = "$%s$" % latex(xac_suat)

            # B2: Viết lại nội dung bài toán và lời giải chi tiết
            noidungcauhoi = (
                "Cho tập hợp $A = \\{%s\\}$. Gọi $S$ là tập hợp các số tự nhiên có $4$ chữ số đôi một khác nhau "
                "được lập thành từ các chữ số của tập $A$. Chọn ngẫu nhiên một số từ $S$, xác suất để số "
                "được chọn mà trong mỗi số luôn luôn có mặt hai chữ số chẵn và hai chữ số lẻ bằng"
                % A_str
            )

            # Lời giải chi tiết không viết tắt
            loigiai = (
                "Số phần tử của tập $S$ là $A_{%s}^4 = %s$. \\\\ "
                "Không gian mẫu là chọn ngẫu nhiên $1$ số từ tập $S$. \\\\ "
                "Suy ra số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = C_{%s}^1 = %s$. \\\\ "
                "Gọi $X$ là biến cố: \"Số được chọn luôn luôn có mặt hai chữ số chẵn và hai chữ số lẻ\". \\\\ "
                "- Số cách chọn hai chữ số chẵn từ %s chữ số chẵn $%s$ là $C_{%s}^2 = %s$ cách. \\\\ "
                "- Số cách chọn hai chữ số lẻ từ %s chữ số lẻ $%s$ là $C_{%s}^2 = %s$ cách. \\\\ "
                "- Từ $4$ chữ số được chọn ta lập số có $4$ chữ số khác nhau, số cách lập tương ứng với một hoán vị của $4$ phần tử nên có $4! = %s$ cách. \\\\ "
                "Suy ra số phần tử của biến cố $X$ là $n\\left(X\\right) = C_{%s}^2 \\cdot C_{%s}^2 \\cdot 4! = %s \\cdot %s \\cdot %s = %s$. \\\\ "
                "Vậy xác suất cần tính $P\\left(X\\right) = \\frac{n\\left(X\\right)}{n\\left(\\Omega\\right)} = \\frac{%s}{%s} = %s$."
                % (
                    n_total, omega, 
                    omega, omega, 
                    n_chan, "{" + "; ".join(map(str, chan)) + "}", n_chan, cach_chon_chan,
                    n_le, "{" + "; ".join(map(str, le)) + "}", n_le, cach_chon_le,
                    hoan_vi,
                    n_chan, n_le, cach_chon_chan, cach_chon_le, hoan_vi, na,
                    na, omega, latex(xac_suat)
                )
            )

            # Chuẩn bị danh sách đáp án để trộn
            list_ans = ["\\True " + da_dung] + distractors
            random.shuffle(list_ans)

            # Xuất nội dung theo cấu trúc mẫu
            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n" + str(noidungcauhoi) + "\n"
                "\\choice \n"
                "{" + str(list_ans[0]) + "}\n"
                "{" + str(list_ans[1]) + "}\n"
                "{" + str(list_ans[2]) + "}\n"
                "{" + str(list_ans[3]) + "}\n"
                "\\loigiai{" + str(loigiai) + "}\n"
                "\\end{ex}\n \\end{minipage} \n\n")
            return content 

