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


def bt_dang1_p2_b1_c1_hh11(self):
            # Khai báo biến
            # Nội dung câu hỏi
            noidungcauhoi = '''Cho hình chóp $S.ABCD$, biết $AB$ cắt $CD$ tại $E$, $AC$ cắt $BD$ tại $F$. \n'''

            hinhve = (
                '\\begin{center}  \n'
                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                    '\\clip(-1.3344696647024945,-3.7818742818134026) rectangle (9.952192386161295,4.710937140906699); \n'
                    '\\draw [line width=1.pt] (9.,0.)-- (2.,-3.); \n'
                    '\\draw [line width=1.pt] (2.,-3.)-- (0.,0.); \n'
                    '\\draw [line width=1.pt] (0.,0.)-- (2.,4.); \n'
                    '\\draw [line width=1.pt] (2.,4.)-- (2.,-3.); \n'
                    '\\draw [line width=1.pt] (4.333333333333334,-2.)-- (2.,4.); \n'
                    '\\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (4.333333333333334,-2.)-- (0.,0.); \n'
                    '\\draw [line width=1.pt] (2.,4.)-- (5.,0.); \n'
                    '\\draw [line width=1.pt] (5.,0.)-- (4.333333333333334,-2.); \n'
                    '\\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (5.,0.)-- (0.,0.); \n'
                    '\\draw [line width=1.pt] (5.,0.)-- (9.,0.); \n'
                    '\\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (5.,0.)-- (2.,-3.); \n'
                    '\\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (3.4210526315789482,-1.5789473684210527)-- (1.4285714285714288,-2.1428571428571432); \n'
                    '\\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (3.4210526315789482,-1.5789473684210527)-- (4.583333333333334,-1.25); \n'
                    '\\draw [line width=1.pt] (4.583333333333334,-1.25)-- (9.,0.); \n'
                    '\\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (2.,4.)-- (3.4210526315789482,-1.5789473684210527); \n'
                    '\\draw (1.7807974073869632,4.760385824590659) node[anchor=north west] {$S$}; \n'
                    '\\draw (-0.5927394094430998,0.5448855405330829) node[anchor=north west] {$A$}; \n'
                    '\\draw (4.94551316316038,0.8044911298738721) node[anchor=north west] {$B$}; \n'
                    '\\draw (4.2779559334269255,-1.828651276296989) node[anchor=north west] {$C$}; \n'
                    '\\draw (1.6077270144931046,-2.8917979755021253) node[anchor=north west] {$D$}; \n'
                    '\\draw (9.07447825077101,0.5448855405330829) node[anchor=north west] {$E$}; \n'
                    '\\draw (3.1,-1.6) node[anchor=north west] {$F$}; \n'
                    '\\draw (0.6,-1.816289105375999) node[anchor=north west] {$G$}; \n'
                    '\\draw [line width=1.pt] (2.,4.)-- (1.4285714285714288,-2.1428571428571432); \n'
                '\\end{tikzpicture}  \n'
            '\\end{center}  \n'
                )

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Đường thẳng $EF$ nằm trong mặt phẳng $(ABCD)$'
            nb_da_1_s = 'Đường thẳng $EF$ không nằm trong mặt phẳng $(ABCD)$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True Điểm $E$ thuộc mặt phẳng $(SAB)$'
            nb_da_2_s = 'Điểm $E$ thuộc mặt phẳng $(SAC)$'
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]
            nb_da_2=random.choice(list_nb_da_2)

            nb_da_3_d = '\\True Điểm $E$ thuộc mặt phẳng $(SCD)$'
            nb_da_3_s = 'Điểm $E$ thuộc mặt phẳng $(SBD)$'
            list_nb_da_3=[nb_da_3_d,nb_da_3_s]
            nb_da_3=random.choice(list_nb_da_3)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1,nb_da_2,nb_da_3]

            # Nội dung lời giải
            loigiai_nb_1 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $E=AB \\cap CD$ nên $E \\in AB$ và $AB \\subset (ABCD)$ suy ra $E \\in (ABCD)$. \\\\ \n'
                            '\\hspace*{1cm} $F=AC \\cap BD$ nên $F \\in AC$ và $AC \\subset (ABCD)$ suy ra $F \\in (ABCD)$. \\\\ \n'
                            'Vậy $EF$ nằm trong mặt phẳng $(ABCD)$.'
                        )
            loigiai_nb_2 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $E=AB \\cap CD$ nên $E \\in AB$ và $AB \\subset (SAB)$ suy ra $E \\in (SAB)$.'
                        )
            loigiai_nb_3 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $E=AB \\cap CD$ nên $E \\in CD$ và $CD \\subset (SCD)$ suy ra $E \\in (SCD)$.'
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1,loigiai_nb_2,loigiai_nb_3]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True $AB$ là giao tuyến của hai mặt phẳng $(SAB)$ và $(ABCD)$'
            th_da_1_s = '$AB$ là giao tuyến của hai mặt phẳng $(SAD)$ và $(ABCD)$'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True $AC$ là giao tuyến của hai mặt phẳng $(SAC)$ và $(ABCD)$'
            th_da_2_s = '$AC$ là giao tuyến của hai mặt phẳng $(SAB)$ và $(ABCD)$'
            list_th_da_2=[th_da_2_d,th_da_2_s]
            th_da_2=random.choice(list_th_da_2)

            th_da_3_d = '\\True $AD$ là giao tuyến của hai mặt phẳng $(SAD)$ và $(ABCD)$'
            th_da_3_s = '$AD$ là giao tuyến của hai mặt phẳng $(SAC)$ và $(ABCD)$'
            list_th_da_3=[th_da_3_d,th_da_3_s]
            th_da_3=random.choice(list_th_da_3)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1,th_da_2,th_da_3]

            # Nội dung lời giải
            loigiai_th_1 = ('Ta thấy $A$ và $B$ là điểm chung của hai mặt phẳng $(SAB)$ và $(ABCD)$ nên $AB=(SAB) \\cap (ABCD)$.'
                        )
            loigiai_th_2 = ('Ta thấy $A$ và $C$ là điểm chung của hai mặt phẳng $(SAC)$ và $(ABCD)$ nên $AC=(SAC) \\cap (ABCD)$.'
                        )
            loigiai_th_3 = ('Ta thấy $A$ và $D$ là điểm chung của hai mặt phẳng $(SAD)$ và $(ABCD)$ nên $AC=(SAD) \\cap (ABCD)$.'
                        )
            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1,loigiai_th_2,loigiai_th_3]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True $SF$ là giao tuyến của hai mặt phẳng $(SAC)$ và $(SBD)$'
            vd_da_1_s = '$SF$ là giao tuyến của hai mặt phẳng $(SAC)$ và $(SBC)$'
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True $SE$ là giao tuyến của hai mặt phẳng $(SAB)$ và $(SCD)$'
            vd_da_2_s = '$SE$ là giao tuyến của hai mặt phẳng $(SAB)$ và $(SAC)$'
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]
            vd_da_2=random.choice(list_vd_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1,vd_da_2]

            # Nội dung lời giải
            loigiai_vd_1 = ('Ta thấy $S$ là một điểm chung của hai mặt phẳng. \\\\ \n'
                            'Ta có \\\\ \n'
                            '\\hspace*{1cm} $\\heva{& F \\in AC, AC \\subset (SAC) \\\\ & F \\in BD, BD \\subset (SBD)} \\Rightarrow F = (SAC) \\cap (SBD)$. \\\\ \n'
                            'Vậy $SF$ là giao tuyến của hai mặt phẳng $(SAC)$ và $(SBD)$.'
                        )
            loigiai_vd_2 = ('Ta thấy $S$ là một điểm chung của hai mặt phẳng. \\\\ \n'
                            'Ta có \\\\ \n'
                            '\\hspace*{1cm} $\\heva{& E \\in AB, AB \\subset (SAB) \\\\ & E \\in CD, CD \\subset (SCD)} \\Rightarrow E = (SAB) \\cap (SCD)$. \\\\ \n'
                            'Vậy $SE$ là giao tuyến của hai mặt phẳng $(SAB)$ và $(SCD)$.'
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1,loigiai_vd_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Gọi $G=EF \\cap AD$, khi đó $SG=(SEF) \\cap (SAD)$'
            vdc_da_1_s = 'Gọi $G=EF \\cap AD$, khi đó $SG=(SEF) \\cap (SAB)$'
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '\\True Gọi $G=EF \\cap AD$, khi đó $G=AD \\cap (SEF)$'
            vdc_da_2_s = 'Gọi $G=EF \\cap AD$, khi đó $G=AD \\cap (SEB)$'
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
            vdc_da_2=random.choice(list_vdc_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1,vdc_da_2]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Ta thấy $S$ là một điểm chung của hai mặt phẳng. \\\\ \n'
                            'Ta có \\\\ \n'
                            '\\hspace*{1cm} $\\heva{& G \\in AD, AD \\subset (SAD) \\\\ & G \\in EF, EF \\subset (SEF)} \\Rightarrow G = (SAD) \\cap (SEF)$. \\\\ \n'
                            'Vậy $EF$ là giao tuyến của hai mặt phẳng $(SAD)$ và $(SEF)$.'
                        )
            loigiai_vdc_2 = (
                            'Ta có \\\\ \n'
                            '\\hspace*{1cm} $\\heva{& G \\in AD \\\\ & G \\in EF, EF \\subset (SEF)} \\Rightarrow G = AD \\cap (SEF)$.'
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1,loigiai_vdc_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
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

