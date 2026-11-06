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


def bt_dang19_p2_b3_c2_ds11(self):
            # Khai báo biến
            # --- B3: KHAI BÁO VÀ NGẪU NHIÊN HÓA CÁC THAM SỐ ---
            a1 = random.choice([100, 120, 140, 150])  # Tiền lương năm thứ nhất PA 1 (triệu)
            d1 = random.choice([12, 15, 18, 20])  # Tăng hàng năm PA 1 (triệu)

            b1 = random.choice([20, 24, 25, 30])  # Tiền lương quý thứ nhất PA 2 (triệu)
            d2_val = random.choice([1.2, 1.5, 1.8, 2.0])  # Tăng hàng quý PA 2 (triệu)
            d2_str = str(d2_val).replace(".", ",")

            # Tính toán các giá trị cho Phương án 1
            u3 = a1 + 2 * d1  # Lương năm thứ 3
            S1_3 = 3 * a1 + 3 * d1  # Tổng lương 3 năm PA 1

            # Tính toán các giá trị cho Phương án 2 (3 năm = 12 quý)
            S2_12_val = 6 * (2 * b1 + 11 * d2_val)
            S2_12_str = str(round(S2_12_val, 2)).replace(".", ",")

            # So sánh 2 phương án
            if S1_3 > S2_12_val:
                best_option = 1
                best_text = "phương án 1"
                worst_text = "phương án 2"
            else:
                best_option = 2
                best_text = "phương án 2"
                worst_text = "phương án 1"

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = (
                "Khi ký kết hợp đồng lao động với người lao động, một doanh nghiệp đề xuất hai phương án trả lương như sau: "
                "{\\bf Phương án 1:} Năm thứ nhất, tiền lương là %s triệu. Kể từ năm thứ hai trở đi, mỗi năm tiền lương được tăng %s triệu. "
                "{\\bf Phương án 2:} Quý thứ nhất, tiền lương là %s triệu. Kể từ quý thứ hai trở đi, mỗi quý tiền lương được tăng %s triệu."
                % (a1, d1, b1, d2_str)
            )

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = (
                "\\True Trong phương án 1: dãy số tiền lương là cấp số cộng có số hạng đầu tiên là $u_1 = %s$, công sai $d_1 = %s$"
                % (a1, d1)
            )
            nb_da_1_s = (
                "Trong phương án 1: dãy số tiền lương là cấp số cộng có số hạng đầu tiên là $u_1 = %s$, công sai $d_1 = %s$"
                % (a1, d1 + 2)
            )
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = (
                "Trong phương án 1, tiền lương mỗi năm tạo thành một cấp số cộng với số hạng đầu tiên $u_1 = %s$ triệu "
                "và công sai $d_1 = %s$ triệu." % (a1, d1)
            )
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = (
                "\\True Trong phương án 1: tiền lương người lao động nhận được trong năm thứ ba là %s triệu"
                % (u3)
            )
            th_da_1_s = (
                "Trong phương án 1: tiền lương người lao động nhận được trong năm thứ ba là %s triệu"
                % (u3 + d1)
            )
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = (
                "Trong phương án 1, tiền lương người lao động nhận được trong năm thứ ba là: \\\\"
                "$u_3 = u_1 + 2d_1 = %s + 2 \\cdot %s = %s$ triệu đồng." % (a1, d1, u3)
            )
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = (
                "\\True Trong phương án 1: tổng tiền lương người lao động nhận được trong ba năm là %s triệu"
                % (S1_3)
            )
            vd_da_1_s = (
                "Trong phương án 1: tổng tiền lương người lao động nhận được trong ba năm là %s triệu"
                % (S1_3 + 20)
            )
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = (
                "Tổng tiền lương người lao động nhận được trong ba năm theo phương án 1 là tổng 3 số hạng đầu của cấp số cộng: \\\\"
                "$S_{1, 3} = \\frac{3}{2} \\cdot [2u_1 + 2d_1] = 3 \\cdot u_1 + 3 \\cdot d_1 = 3 \\cdot %s + 3 \\cdot %s = %s$ triệu đồng."
                % (a1, d1, S1_3)
            )
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = (
                "\\True Nếu ký hợp đồng lao động trong ba năm, với mong muốn nhận được tổng số tiền lương cao nhất thì người lao động nên chọn %s"
                % (best_text)
            )
            vdc_da_1_s = (
                "Nếu ký hợp đồng lao động trong ba năm, với mong muốn nhận được tổng số tiền lương cao nhất thì người lao động nên chọn %s"
                % (worst_text)
            )
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = (
                "Theo phương án 2, tiền lương theo từng quý lập thành một cấp số cộng có số hạng đầu $v_1 = %s$ triệu "
                "và công sai $d_2 = %s$ triệu. \\\\"
                "Trong 3 năm có $3 \\cdot 4 = 12$ quý. Tổng tiền lương nhận được trong 3 năm (12 quý) theo phương án 2 là: \\\\"
                "$S_{2, 12} = \\frac{12}{2} \\cdot [2v_1 + 11d_2] = 6 \\cdot [2 \\cdot %s + 11 \\cdot %s] = %s$ triệu đồng. \\\\"
                "Tổng tiền lương trong 3 năm theo phương án 1 là $S_{1, 3} = %s$ triệu đồng. \\\\"
                "So sánh hai phương án: vì $%s$ triệu đồng %s $%s$ triệu đồng nên người lao động nên chọn %s."
                % (
                    b1,
                    d2_str,
                    b1,
                    d2_str,
                    S2_12_str,
                    S1_3,
                    S1_3,
                    ">" if best_option == 1 else "<",
                    S2_12_str,
                    best_text,
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

