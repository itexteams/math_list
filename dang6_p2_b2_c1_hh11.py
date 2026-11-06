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


def bt_dang6_p2_b2_c1_hh11(self):
    # Nội dung câu hỏi gốc
    noidungcauhoi = (
        """Cho hình chóp $S.ABCD$ có đáy là hình bình hành, $%s$ và $%s$ cắt nhau tại $%s$. Gọi $%s$ là trung điểm $%s$. Mặt phẳng $(%sCD)$ cắt $%s, %s$ lần lượt tại $%s, %s$. Trong mặt phẳng $(CD%s%s)$, gọi $%s$ là giao điểm của $%s%s$ và $%s%s$."""
        % (
            "AC","BD",
            "O",
            "I",
            "SO",
            "I",
            "SA",
            "SB",
            "M",
            "N",
            "M",
            "N",
            "K",
            "C",
            "N",
            "D",
            "M",
        )
    )

    # Khởi tạo mã TikZ hình vẽ chính xác 100% theo quy định
    hinhve = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (1.5,1);
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (4,0);
    \\coordinate (D) at (5.5,1);
    \\coordinate (O) at (2.75,0.5);
    \\coordinate (S) at (3,4);
    \\coordinate (I) at (2.875,2.25);
    \\coordinate (N) at (2,2.667);
    \\coordinate (M) at (2.5,3);
    \\coordinate (E) at (1,1.333);
    \\coordinate (K) at (1,4);
    \\draw[line width=1pt] (S)--(B) (S)--(C) (S)--(D) (B)--(C) (C)--(D) (K)--(S) (K)--(C) (K)--(M);
    \\draw[line width=1pt, dashed] (S)--(A) (A)--(B) (A)--(D) (A)--(C) (B)--(D) (S)--(O) (I)--(D) (I)--(C) (E)--(O) (M)--(D) (N)--(M);
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (O) circle (1pt) node[below] {$O$};
    \\fill (S) circle (1pt) node[above right] {$S$};
    \\fill (I) circle (1pt) node[right] {$I$};
    \\fill (N) circle (1pt) node[left] {$N$};
    \\fill (M) circle (1pt) node[above left] {$M$};
    \\fill (E) circle (1pt) node[left] {$E$};
    \\fill (K) circle (1pt) node[above left] {$K$};
    \\end{tikzpicture}
    \\end{center}"""

    ########################################################################
    # Nhận biết ############################################
    point_nb_s = random.choice(["M", "B", "E"])
    nb_da_1_d = "\\True Giao điểm của $ID$ với mặt phẳng $(SBC)$ là điểm $N$"
    nb_da_1_s = "Giao điểm của $ID$ với mặt phẳng $(SBC)$ là điểm %s" % point_nb_s
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    list_nb_1 = [nb_da_1]

    loigiai_nb_1 = (
        """Ta có $ID$ nằm trong mặt phẳng $(SBD)$. \\\\
    $(SBD) \\cap (SBC)$ theo giao tuyến là $SB$. \\\\
    Kéo dài $ID$ cắt $SB$ tại $N$. \\\\
    $\\Rightarrow N$ là giao điểm của $ID$ với mặt phẳng $(SBC)$."""
        % ()
    )

    list_nb_2 = [loigiai_nb_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ########################################################################
    # Thông hiểu ############################################
    rel_th_s = random.choice(["song song với", "chéo nhau"])
    th_da_1_d = "\\True Hai đường thẳng $OI$ và $SC$ cắt nhau tại $S$"
    th_da_1_s = "$OI$ %s $SC$" % rel_th_s
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    list_th_1 = [th_da_1]

    loigiai_th_1 = (
        """Ta thấy $OI$ nằm trên đường thẳng $SO$ nên $OI$ cắt $SC$ tại $S$.""" % ()
    )

    list_th_2 = [loigiai_th_1]

    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ########################################################################
    # Vận dụng ############################################
    ratio_s = random.choice(["\\frac{2}{3}", "\\frac{1}{2}", "\\frac{3}{4}"])
    vd_da_1_d = "\\True $SN = \\frac{1}{3} SB$"
    vd_da_1_s = "$SN = %s SB$" % ratio_s
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    list_vd_1 = [vd_da_1]

    loigiai_vd_1 = (
        """Gọi $E$ là trung điểm $BN$, $OE$ là đường trung bình của tam giác $BDN \\Rightarrow OE // DN$ và $NE = EB$. \\\\
    Trong tam giác $SOE$, ta có $NI$ qua trung điểm $I$ của $SO$ và $NI // OE$ nên $N$ là trung điểm của $SE$, suy ra $SN = NE$. \\\\
    Vậy $SN = NE = EB$ hay $SN = %s SB$."""
        % ("\\frac{1}{3}")
    )

    list_vd_2 = [loigiai_vd_1]

    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ########################################################################
    # Vận dụng cao ############################################
    rel_vdc_s = random.choice(["chéo nhau", "cắt nhau tại một điểm"])
    vdc_da_1_d = "\\True Hai đường thẳng $SK$ và $BC$ song song với nhau"
    vdc_da_1_s = "Hai đường thẳng $SK$ và $BC$ %s" % rel_vdc_s
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    list_vdc_1 = [vdc_da_1]

    loigiai_vdc_1 = (
        """Dễ thấy $S$ là điểm chung của hai mặt phẳng $(SBC)$ và $(SAD)$. \\\\
    Ta có: $\\begin{cases} K \\in CN, CN \\subset (SBC) \\\\ K \\in DM, DM \\subset (SAD) \\end{cases} \\Rightarrow K \\in (SBC) \\cap (SAD)$. \\\\
    Vì vậy $SK = (SBC) \\cap (SAD)$. \\\\
    Khi đó: $\\begin{cases} SK = (SBC) \\cap (SAD) \\\\ BC \\subset (SBC), AD \\subset (SAD) \\\\ BC // AD \\end{cases} \\Rightarrow SK // %s // AD$. \\\\
    Do đó hai đường thẳng $SK$ và $BC$ song song với nhau."""
        % ("BC")
    )

    list_vdc_2 = [loigiai_vdc_1]

    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)


    def count_true_answers(answers):
        return sum("\\True" in ans for ans in answers)


    # Lặp đến khi số phương án đúng từ 1 đến 3
    while True:
        point_nb_s = random.choice(["M", "B", "E"])
        nb_da_1_d = "\\True Giao điểm của $ID$ với mặt phẳng $(SBC)$ là điểm $N$"
        nb_da_1_s = "Giao điểm của $ID$ với mặt phẳng $(SBC)$ là điểm %s" % point_nb_s
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        rel_th_s = random.choice(["song song với", "chéo nhau"])
        th_da_1_d = "\\True Hai đường thẳng $OI$ và $SC$ cắt nhau tại $S$"
        th_da_1_s = "$OI$ %s $SC$" % rel_th_s
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        ratio_s = random.choice(["\\frac{2}{3}", "\\frac{1}{2}", "\\frac{3}{4}"])
        vd_da_1_d = "\\True $SN = \\frac{1}{3} SB$"
        vd_da_1_s = "$SN = %s SB$" % ratio_s
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        rel_vdc_s = random.choice(["chéo nhau", "cắt nhau tại một điểm"])
        vdc_da_1_d = "\\True Hai đường thẳng $SK$ và $BC$ song song với nhau"
        vdc_da_1_s = "Hai đường thẳng $SK$ và $BC$ %s" % rel_vdc_s
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    # Gán lại vào danh sách sau khi tìm được bộ đáp án hợp lệ
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

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+str(noidungcauhoi)+ 
        '\\choiceTFn \n'
        '{'+str(shuffled_answers_nb[0])+'}\n'
        '{'+str(shuffled_answers_th[0])+'}\n'
        '{'+str(shuffled_answers_vd[0])+'}\n'
        '{'+str(shuffled_answers_vdc[0])+'}\n'
        '\\loigiai{ \n'+hinhve+
        '\\begin{enumEX}[a)]{1} \n'
        '\\item '+str(shuffled_solutions_nb[0])+'\n'
        '\\item '+str(shuffled_solutions_th[0])+'\n'
        '\\item '+str(shuffled_solutions_vd[0])+'\n'
        '\\item '+str(shuffled_solutions_vdc[0])+'\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

