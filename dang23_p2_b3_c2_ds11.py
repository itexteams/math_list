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


def bt_dang23_p2_b3_c2_ds11(self):
            # Khai báo biến
            # --- B3: KHAI BÁO VÀ NGẪU NHIÊN HÓA CÁC THAM SỐ ---
            q = random.choice([2, 3, 4, 5])  # Công bội (bội số tăng mỗi ngày)
            N = random.choice([8, 9, 10, 11, 12])  # Số ngày hồ đầy khi bắt đầu với 1 lá sen
            k = random.choice([2, 3])  # Số mũ giả định cho ngày đầu
            u1_alt = q**k  # Số lá sen ngày đầu ở phương án giả định (ví dụ 3^2 = 9)

            day_alt_correct = N - k  # Ngày đầy hồ đúng
            day_alt_wrong = N - k + 1  # Ngày đầy hồ sai

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = (
                "Trong một hồ sen, số lá sen ngày hôm sau bằng %s lần số lá sen ngày hôm trước. "
                "Biết rằng ngày đầu có 1 lá sen thì tới ngày thứ %s hồ sẽ đầy lá sen. "
                "Hỏi các mệnh đề sau đúng hay sai?" % (q, N)
            )

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = (
                "\\True Số lá sen lập thành cấp số nhân $(u_n)$ với $u_1 = 1$ và công bội $q = %s$"
                % (q)
            )
            nb_da_1_s = (
                "Số lá sen lập thành cấp số nhân $(u_n)$ với $u_1 = 1$ và công bội $q = %s$"
                % (q + 1)
            )
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = (
                "Vì số lá sen ngày hôm sau bằng %s lần số lá sen ngày hôm trước nên số lá sen mỗi ngày lập thành một cấp số nhân $(u_n)$ với $u_1 = 1$ và công bội $q = %s$."
                % (q, q)
            )
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = (
                "\\True Dãy số lá sen $(u_n)$ tăng theo bội số $q = %s$ nên không phải là cấp số cộng"
                % (q)
            )
            th_da_1_s = (
                "Số lá sen lập thành cấp số cộng $(u_n)$ với $u_1 = 1$ và công bội $q = %s$"
                % (q)
            )
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = (
                "Dãy số $(u_n)$ là cấp số nhân với công bội $q = %s \\ne 1$, do đó không phải là cấp số cộng."
                % (q)
            )
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = (
                "\\True Nếu ngày đầu có %s lá sen thì tới ngày thứ %s hồ sẽ đầy lá sen"
                % (u1_alt, day_alt_correct)
            )
            vd_da_1_s = (
                "Nếu ngày đầu có %s lá sen thì tới ngày thứ %s hồ sẽ đầy lá sen"
                % (u1_alt, day_alt_correct - 1)
            )
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = (
                "Số lá sen khi hồ đầy là: $u_{%s} = u_1 \\cdot q^{%s} = 1 \\cdot %s^{%s} = %s^{%s}$ lá. \\\\"
                "Nếu ngày đầu tiên có %s lá sen (tức $%s = %s^{%s}$ lá), gọi $v_m$ là số lá sen ở ngày thứ $m$: \\\\"
                "$v_m = %s \\cdot %s^{m-1} = %s^{%s} \\cdot %s^{m-1} = %s^{m+%s-1}$. \\\\"
                "Để hồ đầy lá sen thì: \\\\"
                "$v_m = u_{%s} \\Leftrightarrow %s^{m+%s-1} = %s^{%s} \\Leftrightarrow m + %s - 1 = %s \\Leftrightarrow m = %s$. \\\\"
                "Vậy tới ngày thứ %s thì hồ sẽ đầy lá sen."
                % (
                    N,
                    N - 1,
                    q,
                    N - 1,
                    q,
                    N - 1,
                    u1_alt,
                    u1_alt,
                    q,
                    k,
                    u1_alt,
                    q,
                    q,
                    k,
                    q,
                    q,
                    k,
                    N,
                    q,
                    k,
                    q,
                    N - 1,
                    k,
                    N - 1,
                    day_alt_correct,
                    day_alt_correct,
                )
            )
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = (
                "\\True Bắt đầu với %s lá sen sẽ giúp hồ đầy nhanh hơn %s ngày so với khi bắt đầu với 1 lá sen"
                % (u1_alt, k)
            )
            vdc_da_1_s = (
                "Nếu ngày đầu có %s lá sen thì tới ngày thứ %s hồ sẽ đầy lá sen"
                % (u1_alt, day_alt_wrong)
            )
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = (
                "Khi bắt đầu với 1 lá sen, hồ đầy sau %s ngày. \\\\"
                "Khi bắt đầu với %s lá sen (bằng $%s^{%s}$ lá), số ngày cần thiết để hồ đầy là $m = %s - %s = %s$ ngày. \\\\"
                "Như vậy, thời gian hồ đầy lá sen giảm đi $%s - %s = %s$ ngày."
                % (N, u1_alt, q, k, N, k, day_alt_correct, N, day_alt_correct, k)
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

