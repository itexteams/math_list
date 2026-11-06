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


def bt_dang20_p2_b3_c2_ds11(self):
            # Khai báo biến
            # --- B3: KHAI BÁO VÀ NGẪU NHIÊN HÓA CÁC THAM SỐ ---
            # Đợt 1: Cấp số cộng
            u1 = random.choice([2, 3, 4, 5])  # Số tiền tháng đầu đợt 1 (triệu)
            d = random.choice([2, 3])  # Công sai (triệu)
            n1 = random.choice([20, 24, 25])  # Số tháng đợt 1

            u10 = u1 + 9 * d  # Số tiền tháng thứ 10
            S1 = n1 * (2 * u1 + (n1 - 1) * d) // 2  # Tổng tiền đợt 1 (triệu)

            # Đợt 2: Cấp số nhân (gấp đôi mỗi tháng -> q = 2)
            v1 = random.choice([3, 4, 5, 6])  # Số tiền tháng đầu đợt 2 (triệu)
            m = random.choice([6, 7, 8])  # Số tháng đợt 2
            q = 2

            S2 = v1 * (2**m - 1)  # Tổng tiền đợt 2 (triệu)

            # Tổng giá trị xe (triệu đồng) và chuyển sang tỉ đồng
            T_trieu = S1 + S2
            T_ti_val = T_trieu / 1000
            T_ti_str = (
                f"{T_ti_val:.3f}".replace(".", ",").rstrip("0").rstrip(",")
                if T_ti_val % 1 != 0
                else str(int(T_ti_val))
            )

            # Tổng số tháng
            tong_thang = n1 + m

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = (
                "Do nhu cầu đi lại của gia đình, anh Bình quyết định thực hiện tích góp tiền để mua một chiếc ô tô HONDA CRV trị giá $%s$ tỉ đồng. \\\\"
                "{\\bf Đợt thứ nhất:} anh Bình đã tích góp theo nguyên tắc tháng sau tích góp nhiều hơn tháng ngay trước đó số tiền là $%s$ triệu đồng và cứ như thế đến tháng thứ 10 anh phải góp $%s$ triệu đồng. Đến hết đợt thứ nhất anh Bình có tất cả $%s$ triệu đồng. \\\\"
                "{\\bf Đợt thứ hai kế tiếp:} do muốn rút ngắn thời gian mua xe thì số tiền còn lại anh tiếp tục tích góp với tháng đầu là $%s$ triệu đồng và mỗi tháng tiếp theo số tiền gấp đôi tháng kế trước nó. \\\\"
                "Các mệnh đề sau đây đúng hay sai?"
                % (T_ti_str, d, u10, S1, v1)
            )

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = (
                "\\True Đợt thứ nhất anh Bình tích lũy tiền theo dãy số với cấp số cộng có công sai là $d = %s$ triệu và $u_1 = %s$ triệu"
                % (d, u1)
            )
            nb_da_1_s = (
                "Đợt thứ nhất anh Bình tích lũy tiền theo dãy số với cấp số cộng có công sai là $d = %s$ triệu và $u_1 = %s$ triệu"
                % (d, u1 + 1)
            )
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = (
                "Đợt thứ nhất, số tiền tích lũy mỗi tháng tăng đều nên lập thành một cấp số cộng với công sai $d = %s$ triệu đồng. \\\\"
                "Ta có $u_{10} = u_1 + 9d \\Leftrightarrow %s = u_1 + 9 \\cdot %s \\Leftrightarrow u_1 = %s$ triệu đồng."
                % (d, u10, d, u1)
            )
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = "\\True Anh Bình tích lũy tiền hết đợt thứ nhất trong $%s$ tháng" % (
                n1
            )
            th_da_1_s = "Anh Bình tích lũy tiền hết đợt thứ nhất trong $%s$ tháng" % (n1 + 1)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            # Biến đổi phương trình bậc 2 tìm n1: d*n^2 + (2*u1 - d)*n - 2*S1 = 0
            A_eq = d
            B_eq = 2 * u1 - d
            C_eq = 2 * S1

            loigiai_th_1 = (
                "Gọi $n$ là số tháng tích lũy ở đợt thứ nhất ($n \\in \\mathbb{N}^*$). \\\\"
                "Tổng số tiền tích lũy đợt thứ nhất là: \\\\"
                "$S_n = \\frac{n[2u_1 + (n - 1)d]}{2} = %s \\Leftrightarrow \\frac{n[2 \\cdot %s + (n - 1) \\cdot %s]}{2} = %s$ \\\\"
                "$\\Leftrightarrow %s n^2 + %s n - %s = 0 \\Leftrightarrow n = %s$ (tháng)."
                % (S1, u1, d, S1, A_eq, B_eq, C_eq, n1)
            )
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = (
                "\\True Đợt thứ hai anh Bình tích lũy tiền theo dãy số với cấp số nhân có công bội là $q = 2$ và $u_1 = %s$ triệu"
                % (v1)
            )
            vd_da_1_s = (
                "Đợt thứ hai anh Bình tích lũy tiền theo dãy số với cấp số nhân có công bội là $q = 2$ và $u_1 = %s$ triệu"
                % (v1 + 1)
            )
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = (
                "Ở đợt thứ hai, số tiền tích góp tháng sau gấp đôi tháng liền trước nên dãy số tiền tích góp từng tháng lập thành một cấp số nhân có công bội $q = 2$ và số hạng đầu $u_1 = %s$ triệu đồng."
                % (v1)
            )
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = (
                "\\True Để đủ tiền mua ô tô thì anh Bình tích góp ít nhất $%s$ tháng"
                % (tong_thang)
            )
            vdc_da_1_s = (
                "Để đủ tiền mua ô tô thì anh Bình tích góp ít nhất $%s$ tháng"
                % (tong_thang - 1)
            )
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            pow_2_m = 2**m
            val_temp = S2 // v1 + 1

            loigiai_vdc_1 = (
                "Đổi $%s$ tỉ đồng bằng $%s$ triệu đồng. \\\\"
                "Số tiền còn lại anh Bình cần tích góp ở đợt thứ hai là: $%s - %s = %s$ triệu đồng. \\\\"
                "Gọi $x$ là số tháng tích góp đợt thứ hai ($x \\in \\mathbb{N}^*$). \\\\"
                "Tổng số tiền tích góp ở đợt thứ hai sau $x$ tháng là: \\\\"
                "$S'_x = v_1 \\cdot \\frac{q^x - 1}{q - 1} = %s \\cdot (2^x - 1)$. \\\\"
                "Để đủ tiền mua xe thì $S'_x \\ge %s \\Leftrightarrow %s \\cdot (2^x - 1) \\ge %s \\Leftrightarrow 2^x \\ge %s = 2^{%s} \\Rightarrow x \\ge %s$. \\\\"
                "Do đó đợt thứ hai cần ít nhất %s tháng. \\\\"
                "Vậy tổng thời gian tích góp ít nhất để đủ tiền mua ô tô là: $%s + %s = %s$ tháng."
                % (
                    T_ti_str,
                    T_trieu,
                    T_trieu,
                    S1,
                    S2,
                    v1,
                    S2,
                    v1,
                    S2,
                    val_temp,
                    m,
                    m,
                    m,
                    n1,
                    m,
                    tong_thang,
                )
            )
            list_vdc_2 = [loigiai_vdc_1]


            def count_true_answers(answers):
                return sum("\\True" in ans for ans in answers)


            # Lặp đến khi đáp án có từ 1 đến 3 đúng
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

