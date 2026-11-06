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


def bt_dang18_p2_b3_c2_ds11(self):
            # Khai báo biến
            # --- B3: KHAI BÁO VÀ NGẪU NHIÊN HÓA CÁC THAM SỐ ---
            N = random.choice([20, 25, 30])  # Tổng số hàng ghế trong nhà hát
            u1 = random.choice([12, 14, 15, 16, 18, 20])  # Số ghế ở hàng thứ nhất
            d = random.choice([2, 3, 4])  # Số ghế hàng sau hơn hàng trước

            u2 = u1 + d
            u3 = u1 + 2 * d

            # Chọn vị trí hàng k để hỏi ở mức Vận dụng (k <= N)
            k = random.choice([15, 18, 20])
            if k > N:
                k = N - 5

            uk = u1 + (k - 1) * d
            SN = N * (2 * u1 + (N - 1) * d) // 2

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = (
                "Một nhà hát có %s hàng ghế với %s ghế ở hàng thứ nhất, %s ghế ở hàng thứ hai, %s ghế ở hàng thứ ba và cứ tiếp tục theo quy luật đó, tức là hàng sau nhiều hơn hàng liền trước nó %s ghế. Gọi $u_n$ là số ghế ở hàng thứ $n$."
                % (N, u1, u2, u3, d)
            )

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = "\\True $u_2 = %s$" % (u2)
            nb_da_1_s = "$u_2 = %s$" % (u2 + 1)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = "Hàng ghế thứ hai có số ghế là $u_2 = %s$." % (u2)
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = "\\True Dãy số $(u_n)$ là cấp số cộng có công sai $d = %s$" % (d)
            th_da_1_s = "Dãy số $(u_n)$ là cấp số cộng có công sai $d = %s$" % (d + 1)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = (
                "Vì hàng sau nhiều hơn hàng liền trước %s ghế nên dãy số $(u_n)$ là một cấp số cộng với số hạng đầu $u_1 = %s$ và công sai $d = %s$."
                % (d, u1, d)
            )
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = "\\True Số ghế ở hàng thứ %s nhỏ hơn %s" % (k, uk + 2)
            vd_da_1_s = "Số ghế ở hàng thứ %s nhỏ hơn %s" % (k, uk)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = (
                "Số ghế ở hàng thứ %s là: \\\\"
                "$u_{%s} = u_1 + (%s - 1)d = %s + %s \\cdot %s = %s$ ghế. \\\\"
                "Do đó, số ghế ở hàng thứ %s bằng %s." % (k, k, k, u1, k - 1, d, uk, k, uk)
            )
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = "\\True Tổng số ghế trong nhà hát nhiều hơn %s" % (SN - 10)
            vdc_da_1_s = "Tổng số ghế trong nhà hát nhiều hơn %s" % (SN)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = (
                "Tổng số ghế trong nhà hát chính là tổng của %s số hạng đầu tiên của cấp số cộng $(u_n)$: \\\\"
                "$S_{%s} = \\frac{%s}{2} \\cdot \\left[ 2u_1 + (%s - 1)d \\right] = \\frac{%s}{2} \\cdot \\left[ 2 \\cdot %s + %s \\cdot %s \\right] = %s$ ghế."
                % (N, N, N, N, N, u1, N - 1, d, SN)
            )
            list_vdc_2 = [loigiai_vdc_1]


            def count_true_answers(answers):
                return sum("\\True" in ans for ans in answers)


            # Vòng lặp đảm bảo có từ 1 đến 3 đáp án đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n"
                + str(noidungcauhoi)
                + "\n\\choiceTFn \n"
                "{" + str(shuffled_answers_nb[0]) + "}\n"
                "{" + str(shuffled_answers_th[0]) + "}\n"
                "{" + str(shuffled_answers_vd[0]) + "}\n"
                "{" + str(shuffled_answers_vdc[0]) + "}\n"
                "\\loigiai{ \n"
                "\\begin{enumEX}[a)]{1} \n"
                "\\item " + str(shuffled_solutions_nb[0]) + "\n"
                "\\item " + str(shuffled_solutions_th[0]) + "\n"
                "\\item " + str(shuffled_solutions_vd[0]) + "\n"
                "\\item " + str(shuffled_solutions_vdc[0]) + "\n"
                "\\end{enumEX}} \n"
                "\\end{ex}\n \\end{minipage}\n\n")
            return content

