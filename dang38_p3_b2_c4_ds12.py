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


def bt_dang38_p3_b2_c4_ds12(self):
            # Khai báo biến
            # Tỉ lệ bò mắc bệnh P(M)
            p_m_val = random.randint(15, 35)  # Ví dụ: 15% đến 35%
            # Độ nhạy P(N|M)
            p_n_m_val = random.randint(80, 95) # Ví dụ: 80% đến 95%
            # Xác suất dương tính giả P(N|notM)
            p_n_notm_val = random.randint(5, 12) # Ví dụ: 5% đến 12%

            # Chuyển sang số hữu tỉ để tính toán chính xác
            P_M = Rational(p_m_val, 100)
            P_notM = 1 - P_M
            P_N_M = Rational(p_n_m_val, 100)
            P_N_notM = Rational(p_n_notm_val, 100)

            # Tính xác suất hậu nghiệm P(M|N) theo công thức Bayes
            # P(M|N) = (P(M)*P(N|M)) / (P(M)*P(N|M) + P(notM)*P(N|notM))
            tu_so = P_M * P_N_M
            mau_so = (P_M * P_N_M) + (P_notM * P_N_notM)
            ket_qua_hanh_phan_tram = tu_so / mau_so

            # Làm tròn đến hàng phần trăm (2 chữ số thập phân)
            kq_float = float(ket_qua_hanh_phan_tram)
            kq_rounded = Decimal(str(kq_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            kq_str = str(kq_rounded).replace('.', ',')

            # --- BƯỚC 4: TẠO CÁC PHƯƠNG ÁN SAI ---
            list_distractors = []
            while len(list_distractors) < 3:
                # Tạo các sai số ngẫu nhiên quanh đáp án đúng
                offset = random.choice([-0.15, -0.1, -0.05, 0.05, 0.1, 0.15])
                wrong_val = Decimal(str(kq_float + offset)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                wrong_str = str(wrong_val).replace('.', ',')

                if wrong_str != kq_str and wrong_str not in list_distractors and float(wrong_val) > 0:
                    list_distractors.append(wrong_str)

            # --- BƯỚC 2: VIẾT LẠI BÀI TOÁN THEO MẪU ---

            # Nội dung câu hỏi
            noidungcauhoi = (
                "Tại địa phương A, người ta tiến hành một đợt kiểm tra diện rộng các con bò để phát hiện một loại bệnh X. "
                "Có một loại xét nghiệm Z cho kết quả như sau: Xét nghiệm có độ nhạy %s\\%% (Độ nhạy là xác suất chọn được một mẫu dương tính biết rằng mẫu bị nhiễm bệnh); "
                "xác suất dương tính giả là %s\\%% (Dương tính giả là xét nghiệm dương tính nhưng thực tế không bị nhiễm bệnh). "
                "Biết rằng tỉ lệ bò ở địa phương A bị mắc bệnh X là %s\\%%. "
                "Chọn ngẫu nhiên một con bò ở địa phương A để xét nghiệm, xác suất để chọn được con bò bị nhiễm bệnh, biết rằng con bò có kết quả dương tính với xét nghiệm bằng bao nhiêu? (Kết quả làm tròn đến hàng phần trăm)."
                % (p_n_m_val, p_n_notm_val, p_m_val)
            )

            # Lời giải chi tiết
            loigiai = (
                "Gọi M là biến cố \"Chọn được một con bò bị nhiễm bệnh\".\\\\ "
                "N là biến cố \"Chọn được một con bò dương tính với xét nghiệm\".\\\\ "
                "Theo giả thiết bài toán, ta có: $P(M) = %s$; $P(N|M) = %s$; $P(N|\\overline{M}) = %s$.\\\\ "
                "Suy ra $P(\\overline{M}) = 1 - P(M) = 1 - %s = %s$.\\\\ "
                "Xác suất để con bò bị nhiễm bệnh khi biết nó có kết quả dương tính là $P(M|N)$.\\\\ "
                "Áp dụng công thức Bayes, ta có:\\\\ "
                "$$P(M|N) = \\frac{P(M) \\cdot P(N|M)}{P(M) \\cdot P(N|M) + P(\\overline{M}) \\cdot P(N|\\overline{M})}$$ "
                "$$P(M|N) = \\frac{%s \\cdot %s}{%s \\cdot %s + %s \\cdot %s} \\approx %s.$$"
                % (
                    str(float(P_M)).replace('.', ','), 
                    str(float(P_N_M)).replace('.', ','), 
                    str(float(P_N_notM)).replace('.', ','),
                    str(float(P_M)).replace('.', ','), 
                    str(float(P_notM)).replace('.', ','),
                    str(float(P_M)).replace('.', ','), 
                    str(float(P_N_M)).replace('.', ','),
                    str(float(P_M)).replace('.', ','), 
                    str(float(P_N_M)).replace('.', ','),
                    str(float(P_notM)).replace('.', ','),
                    str(float(P_N_notM)).replace('.', ','),
                    kq_str
                )
            )

            # Trình bày các lựa chọn
            da_dung = "\\True $" + kq_str + "$"
            list_ans = [da_dung, "$" + list_distractors[0] + "$", "$" + list_distractors[1] + "$", "$" + list_distractors[2] + "$"]
            random.shuffle(list_ans)

            # Xuất nội dung theo cấu trúc yêu cầu (không dùng tiền tố r)
            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n" + noidungcauhoi + "\n"
                "\\choice \n"
                "{" + list_ans[0] + "}\n"
                "{" + list_ans[1] + "}\n"
                "{" + list_ans[2] + "}\n"
                "{" + list_ans[3] + "}\n"
                "\\loigiai{" + loigiai + "}\n"
                "\\end{ex}\n"
                "\\end{minipage} \n\n")
            return content

