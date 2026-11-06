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


def bt_dang20_p2_b1_c2_hh11(self):
            # Khai báo biến
            # --- Nội dung câu hỏi ---
            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thoi. Gọi $M, N$ theo thứ tự là trung điểm của các đoạn thẳng $SB, SD$.''')

            ########################################################################
            # Nhận biết ############################################
            # Mệnh đề (a): Về quan hệ song song giữa MN và BD
            nb_da_1_d = '\\True $MN \\parallel BD$'
            nb_da_1_s = '$MN$ cắt $BD$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Trong tam giác $SBD$, ta có $M$ là trung điểm của $SB$ và $N$ là trung điểm của $SD$. \\\\
            Theo tính chất đường trung bình của tam giác, ta có $MN \\parallel BD$.''')

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu ############################################
            # Mệnh đề (b): Về vị trí tương đối giữa MN và AC
            th_da_1_d = '\\True $MN$ và $AC$ là hai đường thẳng chéo nhau'
            th_da_1_s = '$MN$ và $AC$ là hai đường thẳng song song'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Đường thẳng $MN$ nằm trong mặt phẳng $(SBD)$. \\\\
            Đường thẳng $AC$ nằm trong mặt phẳng đáy $(ABCD)$. \\\\
            Mặt phẳng $(SBD)$ và đường thẳng $AC$ có duy nhất một điểm chung là tâm $O$ của hình thoi (giao điểm của $AC$ và $BD$). \\\\
            Vì điểm $O$ không thuộc đường thẳng $MN$ nên $MN$ và $AC$ là hai đường thẳng chéo nhau.''')

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng ############################################
            # Mệnh đề (c): Tính chất hình thoi AC vuông góc BD
            vd_da_1_d = '\\True $AC \\perp BD$'
            vd_da_1_s = '$AC$ không vuông góc với $BD$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Vì đáy $ABCD$ là hình thoi nên hai đường chéo vuông góc với nhau tại trung điểm mỗi đường. \\\\
            Do đó, ta có $AC \\perp BD$.''')

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao ############################################
            # Mệnh đề (d): Góc giữa MN và AC
            vdc_da_1_d = '\\True $(MN, AC) = 90^\\circ$'
            vdc_da_1_s = '$(MN, AC) = 60^\\circ$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Ta có $MN \\parallel BD$ (chứng minh ở câu a). \\\\
            Do đó, góc giữa hai đường thẳng $MN$ và $AC$ bằng góc giữa hai đường thẳng $BD$ và $AC$. \\\\
            Vì $AC \\perp BD$ (tính chất hình thoi) nên $(BD, AC) = 90^\\circ$. \\\\
            Suy ra $(MN, AC) = 90^\\circ$.''')

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán vào list để xử lý
            combined_nb = [(nb_sel, loigiai_nb_1)]
            combined_th = [(th_sel, loigiai_th_1)]
            combined_vd = [(vd_sel, loigiai_vd_1)]
            combined_vdc = [(vdc_sel, loigiai_vdc_1)]

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Vẽ hình TikZ
            hinh_ve_tikz = ('''\\begin{tikzpicture}[scale=0.8, line join=round, line cap=round]
            \\coordinate (A) at (0,0);
            \\coordinate (B) at (-1.5,-1.5);
            \\coordinate (D) at (4,0);
            \\coordinate (C) at ($(B)+(D)-(A)$);
            \\coordinate (S) at (1.2,4);
            \\coordinate (O) at (intersection of A--C and B--D);
            \\coordinate (M) at ($(S)!0.5!(B)$);
            \\coordinate (N) at ($(S)!0.5!(D)$);
            \\draw (S)--(B)--(C)--(D)--(S)--(C);
            \\draw[dashed] (S)--(A)--(B) (A)--(D) (B)--(D) (A)--(C) (M)--(N);
            \\fill (S)  node[above]{$S$};
            \\fill (A)  node[above left]{$A$};
            \\fill (B)  node[below left]{$B$};
            \\fill (C)  node[below right]{$C$};
            \\fill (D)  node[right]{$D$};
            \\fill (M)  node[left]{$M$};
            \\fill (N)  node[above right]{$N$};
            \\end{tikzpicture}''')

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n' +
                '\\begin{center}\n' + hinh_ve_tikz + '\n\\end{center}\n' +
                '\\choiceTFn \n'
                '{' + str(shuffled_answers_nb[0]) + '}\n'
                '{' + str(shuffled_answers_th[0]) + '}\n'
                '{' + str(shuffled_answers_vd[0]) + '}\n'
                '{' + str(shuffled_answers_vdc[0]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

