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


def bt_dang26_p4_b2_c6_ds10(self):
            #Khai báo biến
            # n_de: số câu dễ, n_tb: số câu trung bình, n_kho: số câu khó
            n_de = random.randint(12, 16)
            n_tb = random.randint(8, 12)
            n_kho = random.randint(4, 6)
            n_tong = n_de + n_tb + n_kho

            # Tính không gian mẫu: chọn 5 câu từ tổng số câu
            n_omega = binomial(n_tong, 5)

            # Tính số kết quả thuận lợi cho biến cố A: Đề thi "Tốt"
            # Điều kiện: có cả 3 loại và số câu dễ >= 2. Các bộ (Dễ, TB, Khó) thỏa mãn:
            # TH1: 3 Dễ, 1 TB, 1 Khó
            th1 = binomial(n_de, 3) * binomial(n_tb, 1) * binomial(n_kho, 1)
            # TH2: 2 Dễ, 2 TB, 1 Khó
            th2 = binomial(n_de, 2) * binomial(n_tb, 2) * binomial(n_kho, 1)
            # TH3: 2 Dễ, 1 TB, 2 Khó
            th3 = binomial(n_de, 2) * binomial(n_tb, 1) * binomial(n_kho, 2)

            n_A = th1 + th2 + th3
            xac_suat = Rational(n_A, n_omega)

            # Tạo các đáp án sai
            s = set()
            while len(s) < 3:
                # Tạo các phân số ngẫu nhiên lân cận đáp án đúng bằng cách thay đổi tử số hoặc mẫu số
                sai_tu = n_A + random.randint(-500, 500)
                sai_mau = n_omega + random.randint(-500, 500)
                if sai_tu > 0 and sai_mau > 0:
                    ps_sai = simplify(Rational(sai_tu, sai_mau))
                    if ps_sai != xac_suat:
                        s.add("$%s$" % latex(ps_sai))

            list_sai = list(s)
            da_dung = "$%s$" % latex(xac_suat)

            # Câu hỏi
            noidungcauhoi = (
                "Một bộ đề thi toán học sinh giỏi lớp 12 mà mỗi đề gồm 5 câu được chọn từ %s câu dễ, %s câu trung bình, %s câu khó. "
                "Một đề thi được gọi là \"Tốt\" nếu trong đề thi có cả ba câu dễ, trung bình và khó, đồng thời số câu dễ không ít hơn 2. "
                "Lấy ngẫu nhiên một đề thi trong bộ đề trên. Tính xác suất để đề thi lấy ra là một đề thi \"Tốt\"."
                % (latex(n_de), latex(n_tb), latex(n_kho))
            )

            # Các đáp án
            da_d = "\\True " + str(da_dung)
            da_s1 = str(list_sai[0])
            da_s2 = str(list_sai[1])
            da_s3 = str(list_sai[2])

            # Đưa các đáp án vào danh sách và xáo trộn
            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Nội dung lời giải
            loigiai = (
                "Số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = C_{%s}^{5} = %s$. \\\\ "
                "Gọi $A$ là biến cố \"Đề thi lấy ra là một đề thi tốt\". \\\\ "
                "Vì trong một đề thi \"Tốt\" có cả ba loại câu dễ, trung bình, khó, đồng thời số câu dễ không ít hơn 2 nên ta có các trường hợp sau đây thuận lợi cho biến cố $A$: \\\\ "
                "+ Đề thi gồm 3 câu dễ, 1 câu trung bình và 1 câu khó: có $C_{%s}^{3} \\cdot C_{%s}^{1} \\cdot C_{%s}^{1} = %s$ đề. \\\\ "
                "+ Đề thi gồm 2 câu dễ, 2 câu trung bình và 1 câu khó: có $C_{%s}^{2} \\cdot C_{%s}^{2} \\cdot C_{%s}^{1} = %s$ đề. \\\\ "
                "+ Đề thi gồm 2 câu dễ, 1 câu trung bình và 2 câu khó: có $C_{%s}^{2} \\cdot C_{%s}^{1} \\cdot C_{%s}^{2} = %s$ đề. \\\\ "
                "Suy ra số phần tử của $A$ là $n\\left(A\\right) = %s + %s + %s = %s$. \\\\ "
                "Vậy xác suất cần tính $P\\left(A\\right) = \\frac{%s}{%s} = %s$."
                % (
                    latex(n_tong), latex(n_omega),
                    latex(n_de), latex(n_tb), latex(n_kho), latex(th1),
                    latex(n_de), latex(n_tb), latex(n_kho), latex(th2),
                    latex(n_de), latex(n_tb), latex(n_kho), latex(th3),
                    latex(th1), latex(th2), latex(th3), latex(n_A),
                    latex(n_A), latex(n_omega), latex(xac_suat)
                )
            )

            # Xuất nội dung theo cấu trúc yêu cầu
            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n" + str(noidungcauhoi) + "\n"
                "\\loigiai{" + str(loigiai) + "}\n"
                "\\end{ex}\n \\end{minipage} \n\n")
            return content 

