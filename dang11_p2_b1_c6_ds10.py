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


def bt_dang11_p2_b1_c6_ds10(self):
            # Khai báo biến
            # B2 & B3: Viết code và random bài toán
            so_lan = randint(3,6)
            n_omega = 2**so_lan

            # Nội dung câu hỏi
            noidungcauhoi = ('''Gieo %s lần một đồng tiền hai mặt sấp, ngửa.''' %(latex(so_lan)))

            ########################################################################
            # Nhận biết (Câu a) ############################################
            nb_da_1_d = '\\True $n\\left(\\Omega\\right) = %s$' % (latex(n_omega))
            nb_da_1_s = '$n\\left(\\Omega\\right) = %s$' % (latex(n_omega + 2))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Mỗi lần gieo có $2$ kết quả xảy ra (sấp hoặc ngửa). 
            Gieo $%s$ lần liên tiếp, theo quy tắc nhân ta có số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = 2^{%s} = %s$.''' 
                            % (latex(so_lan), latex(so_lan), latex(n_omega)))

            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu (Câu b) ############################################
            so_kq_A = 2**(so_lan - 1)
            th_da_1_d = '\\True Số kết quả thuận lợi của biến cố $A$: "Lần đầu tiên xuất hiện mặt ngửa" bằng %s' % (latex(so_kq_A))
            th_da_1_s = 'Số kết quả thuận lợi của biến cố $A$: "Lần đầu tiên xuất hiện mặt ngửa" bằng %s' % (latex(so_kq_A - 4))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Biến cố $A$ xảy ra khi lần gieo đầu tiên là mặt ngửa (có $1$ cách chọn). 
            $%s$ lần gieo còn lại mỗi lần có $2$ cách chọn. 
            Vậy số kết quả thuận lợi cho biến cố $A$ là $n\\left(A\\right) = 1 \\cdot 2^{%s} = %s$.''' 
                            % (latex(so_lan), latex(so_lan - 1), latex(so_kq_A)))

            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng (Câu c) ############################################
            so_kq_B = n_omega - 1
            vd_da_1_d = '\\True Số kết quả thuận lợi của biến cố $B$: "Mặt sấp xuất hiện ít nhất một lần" bằng %s' % (latex(so_kq_B))
            vd_da_1_s = 'Số kết quả thuận lợi của biến cố $B$: "Mặt sấp xuất hiện ít nhất một lần" bằng 30'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Xét biến cố đối $\\overline{B}$: "Mặt sấp không xuất hiện lần nào", tức là cả $%s$ lần đều xuất hiện mặt ngửa. 
            Ta có $n\\left(\\overline{B}\\right) = 1$. 
            Số kết quả thuận lợi của biến cố $B$ là $n\\left(B\\right) = n\\left(\\Omega\\right) - n\\left(\\overline{B}\\right) = %s - 1 = %s$.''' 
                            % (latex(so_lan), latex(n_omega), latex(so_kq_B)))

            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao (Câu d) ############################################
            # Sử dụng math.comb để tính tổ hợp vì nó ổn định với số nguyên
            so_kq_C = sum(math.comb(so_lan, k) for k in range(3, 6))
            vdc_da_1_d = '\\True Số kết quả thuận lợi của biến cố $C$: "Số lần mặt sấp xuất hiện nhiều hơn mặt ngửa" bằng %s' % (latex(so_kq_C))
            vdc_da_1_s = 'Số kết quả thuận lợi của biến cố $C$: "Số lần mặt sấp xuất hiện nhiều hơn mặt ngửa" bằng 10'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Số lần sấp nhiều hơn số lần ngửa khi số lần sấp thuộc tập $\\left\\{3; 4; 5\\right\\}$. \\\\
            - Trường hợp 1: Có $3$ lần sấp và $2$ lần ngửa, số kết quả là $C_{%s}^{3} = 10$. \\\\
            - Trường hợp 2: Có $4$ lần sấp và $1$ lần ngửa, số kết quả là $C_{%s}^{4} = 5$. \\\\
            - Trường hợp 3: Có $5$ lần sấp và $0$ lần ngửa, số kết quả là $C_{%s}^{5} = 1$. \\\\
            Vậy số kết quả thuận lợi cho biến cố $C$ là $10 + 5 + 1 = %s$.''' 
                             % (latex(so_lan), latex(so_lan), latex(so_lan), latex(so_kq_C)))

            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

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

            # Gán vào danh sách xáo trộn (mô phỏng theo mẫu python)
            shuffled_answers_nb = [nb_da_1]
            shuffled_solutions_nb = [loigiai_nb_1]
            shuffled_answers_th = [th_da_1]
            shuffled_solutions_th = [loigiai_th_1]
            shuffled_answers_vd = [vd_da_1]
            shuffled_solutions_vd = [loigiai_vd_1]
            shuffled_answers_vdc = [vdc_da_1]
            shuffled_solutions_vdc = [loigiai_vdc_1]

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

