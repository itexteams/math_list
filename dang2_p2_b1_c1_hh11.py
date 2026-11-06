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


def bt_dang2_p2_b1_c1_hh11(self):
            # Khai báo biến

            # Nội dung câu hỏi
            noidungcauhoi = '''Cho tứ diện $ABCD$. Gọi $I, J$ là trung điểm của $AD, BC$, $M$ là điểm thuộc cạnh $AB$, $N$ là một điểm trên cạnh $AC$. \n'''

            hinhve = (
            '\\begin{center}  \n'
                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                    '\\clip(-0.8487300294728501,-2.8747275339285205) rectangle (5.625410665182811,4.5301348087740045);  \n'
                    '\\draw [line width=1.pt] (0.,0.)-- (2.0409108416723893,3.723851818711374);  \n'
                    '\\draw [line width=1.pt] (2.0409108416723893,3.723851818711374)-- (5.,0.);  \n'
                    '\\draw [line width=1.pt] (0.,0.)-- (2.0409108416723893,-2.276148181288626);  \n'
                    '\\draw [line width=1.pt] (2.0409108416723893,-2.276148181288626)-- (5.,0.);  \n'
                    '\\draw [line width=1.pt] (2.0409108416723893,3.723851818711374)-- (2.0409108416723893,-2.276148181288626);  \n'
                    '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (3.5204554208361944,1.861925909355687)-- (1.0204554208361947,-1.138074090644313);  \n'
                    '\\draw [line width=1.pt] (1.314299169524407,2.39807406224262)-- (2.0409108416723893,0.6129217186426961);  \n'
                    '\\draw [line width=1.pt] (2.0409108416723893,3.723851818711374)-- (1.0204554208361947,-1.138074090644313);  \n'
                    '\\draw [line width=1.pt] (2.0409108416723893,0.6129217186426961)-- (5.,0.);  \n'
                    '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.314299169524407,2.39807406224262)-- (5.,0.);  \n'
                    '\\draw [line width=1.pt] (3.5204554208361944,1.861925909355687)-- (2.0409108416723893,-2.276148181288626);  \n'
                    '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (3.5204554208361944,1.861925909355687);  \n'
                    '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.0204554208361947,-1.138074090644313)-- (5.,0.);  \n'
                    '\\draw (1.7,4.3) node[anchor=north west] {A};  \n'
                    '\\draw (-0.5,0.1) node[anchor=north west] {B};  \n'
                    '\\draw (1.922979493831548,-2.3) node[anchor=north west] {C};  \n'
                    '\\draw (5.134480565114135,0.009486803974949007) node[anchor=north west] {D};  \n'
                    '\\draw (3.6105517128176206,2.3) node[anchor=north west] {I};  \n'
                    '\\draw (0.5,-1) node[anchor=north west] {J};  \n'
                    '\\draw (0.7570205061684433,2.9) node[anchor=north west] {M};  \n'
                    '\\draw (1.4,0.9) node[anchor=north west] {N};  \n'
                    '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (5.,0.);  \n'
                    '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.758057838711736,1.4587031322723496)-- (3.002655491537666,0.4137137353239386);  \n'
                    '\\draw (2.9,0.4) node[anchor=north west] {E};  \n'
                    '\\draw (2.669602354352659,2.1) node[anchor=north west] {F};  \n'
                '\\end{tikzpicture}  \n'
            '\\end{center} \n'
                )

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $MN$ là giao tuyến của hai mặt phẳng $(ABC)$ và $(MND)$'
            nb_da_1_s = '$MN$ là giao tuyến của hai mặt phẳng $(ABD)$ và $(MND)$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True $IJ$ là giao tuyến của hai mặt phẳng $(ADJ)$ và $(BCI)$'
            nb_da_2_s = '$IJ$ là giao tuyến của hai mặt phẳng $(ADJ)$ và $(BCM)$'
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]
            nb_da_2=random.choice(list_nb_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1,nb_da_2]

            # Nội dung lời giải
            loigiai_nb_1 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $M \\in AB$ và $AB \\subset (ABC)$ suy ra $M \\in (ABC)$. \\\\ \n'
                            '\\hspace*{1cm} $N \\in AC$ và $AC \\subset (ABC)$ suy ra $N \\in (ABC)$. \\\\ \n'
                            'Vậy $MN$ là giao tuyến của hai mặt phẳng $(ABC)$ và $(MND)$.'
                        )
            loigiai_nb_2 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $I \\in AD$ và $AD \\subset (ADJ)$ suy ra $I \\in (ADJ)$. \\\\ \n'
                            '\\hspace*{1cm} $J \\in BC$ và $BC \\subset (BCI)$ suy ra $J \\in (BCJ)$. \\\\ \n'
                            'Vậy $IJ$ là giao tuyến của hai mặt phẳng $(ADJ)$ và $(BCI)$.'
                        )
            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1,loigiai_nb_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True $AJ$ là giao tuyến của hai mặt phẳng $(ABC)$ và $(ADJ)$'
            th_da_1_s = '$AJ$ là giao tuyến của hai mặt phẳng $(ABC)$ và $(ADC)$'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True $DJ$ là giao tuyến của hai mặt phẳng $(BCD)$ và $(ADJ)$'
            th_da_2_s = '$DJ$ là giao tuyến của hai mặt phẳng $(ABC)$ và $(ADC)$'
            list_th_da_2=[th_da_2_d,th_da_2_s]
            th_da_2=random.choice(list_th_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1,th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('Ta có \\\\ \n'
                            '$A$ là một điểm chung của hai mặt phẳng. \\\\ \n'
                            '\\hspace*{1cm} $J \\in (ADJ)$. \\\\ \n'
                            '\\hspace*{1cm} $J \\in BC$ và $BC \\subset (ABC)$ suy ra $J \\in (ABC)$. \\\\ \n'
                            '$AJ$ là giao tuyến của hai mặt phẳng $(ABC)$ và $(ADJ)$.'
                        )
            loigiai_th_2 = ('Ta có \\\\ \n'
                            '$D$ là một điểm chung của hai mặt phẳng. \\\\ \n'
                            '\\hspace*{1cm} $J \\in (ADJ)$. \\\\ \n'
                            '\\hspace*{1cm} $J \\in BC$ và $BC \\subset (BCD)$ suy ra $J \\in (BCD)$. \\\\ \n'
                            '$DJ$ là giao tuyến của hai mặt phẳng $(BCD)$ và $(ADJ)$.'
                        )
            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1,loigiai_th_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True $ND$ là giao tuyến của hai mặt phẳng $(MND)$ và $(ADC)$'
            vd_da_1_s = '$ND$ là giao tuyến của hai mặt phẳng $(MND)$ và $(ABC)$'
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True $MD$ là giao tuyến của hai mặt phẳng $(MND)$ và $(ABD)$'
            vd_da_2_s = '$MD$ là giao tuyến của hai mặt phẳng $(MND)$ và $(ABC)$'
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]
            vd_da_2=random.choice(list_vd_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1,vd_da_2]

            # Nội dung lời giải
            loigiai_vd_1 = ('Ta thấy $D$ là một điểm chung của hai mặt phẳng. \\\\ \n'
                            'Ta có \\\\ \n'
                            '\\hspace*{1cm} $N \\in (MND)$. \\\\ \n'
                            '\\hspace*{1cm} $N \\in AC$ và $AC \\subset (ACD)$ suy ra $N \\in (ACD)$. \\\\ \n'
                            '$ND$ là giao tuyến của hai mặt phẳng $(MND)$ và $(ADC)$.'
                        )
            loigiai_vd_2 = ('Ta thấy $D$ là một điểm chung của hai mặt phẳng. \\\\ \n'
                            'Ta có \\\\ \n'
                            '\\hspace*{1cm} $M \\in (MND)$. \\\\ \n'
                            '\\hspace*{1cm} $M \\in AB$ và $AB \\subset (ABD)$ suy ra $M \\in (ABD)$. \\\\ \n'
                            '$MD$ là giao tuyến của hai mặt phẳng $(MND)$ và $(ABD)$.'
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
            vdc_da_1_d = '\\True $BI$ là giao tuyến của hai mặt phẳng $(BCI)$ và $(ABD)$'
            vdc_da_1_s = '$BI$ là giao tuyến của hai mặt phẳng $(BCI)$ và $(ABC)$'
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '\\True $E=CI \\cap ND, F=BI \\cap MD$ suy ra $EF=(BCI) \\cap (MND)$'
            vdc_da_2_s = '$E=CI \\cap ND, F=BI \\cap MD$ suy ra $EF=(BCI) \\cap (MNA)$'
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
            vdc_da_2=random.choice(list_vdc_da_2)

            vdc_da_3_d = '\\True $CI$ là giao tuyến của hai mặt phẳng $(BCI)$ và $(ACD)$'
            vdc_da_3_s = '$CI$ là giao tuyến của hai mặt phẳng $(BCI)$ và $(ABC)$'
            list_vdc_da_3=[vdc_da_3_d,vdc_da_3_s]
            vdc_da_3=random.choice(list_vdc_da_3)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1,vdc_da_2,vdc_da_3]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Ta thấy $B$ là một điểm chung của hai mặt phẳng. \\\\ \n'
                            'Ta có \\\\ \n'
                            '\\hspace*{1cm} $I \\in (BCI)$. \\\\ \n'
                            '\\hspace*{1cm} $I \\in AD$ và $AD \\subset (ABD)$ suy ra $I \\in (ABD)$. \\\\ \n'
                            '$BI$ là giao tuyến của hai mặt phẳng $(BCI)$ và $(ABD)$.'
                        )
            loigiai_vdc_2 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $E \\in CI$ và $CI \\subset (BCI)$ suy ra $E \\in (BCI)$. \\\\ \n'
                            '\\hspace*{1cm} $E \\in ND$ và $ND \\subset (MND)$ suy ra $E \\in (MND)$. \\\\ \n'
                            '\\hspace*{1cm} $F \\in BI$ và $BI \\subset (BCI)$ suy ra $F \\in (BCI)$. \\\\ \n'
                            '\\hspace*{1cm} $F \\in MD$ và $MD \\subset (MND)$ suy ra $F \\in (MND)$. \\\\ \n'
                            'Vậy $EF=(BCI) \\cap (MND)$.'
                        )
            loigiai_vdc_3 = ('Ta thấy $C$ là một điểm chung của hai mặt phẳng. \\\\ \n'
                            'Ta có \\\\ \n'
                            '\\hspace*{1cm} $I \\in (BCI)$. \\\\ \n'
                            '\\hspace*{1cm} $I \\in AD$ và $AD \\subset (ACD)$ suy ra $I \\in (ACD)$. \\\\ \n'
                            '$CI$ là giao tuyến của hai mặt phẳng $(BCI)$ và $(ACD)$.'
                            )
            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1,loigiai_vdc_2,loigiai_vdc_3]

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

